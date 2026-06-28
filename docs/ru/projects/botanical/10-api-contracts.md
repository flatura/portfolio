## API-контракты

### Подход к проектированию API

Backend предоставляет REST/JSON API для управления живыми коллекциями растений в мульти-тенантной SaaS-среде. API-контракты организованы вокруг доменных возможностей: учёт растений, поиск по таксономии, массовые операции, импорт, публичные страницы, доступ к медиа и сценарии обмена.

Безопасность обеспечивается на нескольких уровнях:

* JWT-аутентификация через Spring Security.
* Method-level authorization для чувствительных операций.
* Изоляция тенантов через контекст организации / корневого тенанта.
* Фильтрация данных на уровне владения тенантом.
* Bean Validation для request DTO.
* Контролируемые public DTO для анонимных endpoints.
* Soft delete для обратимых удалений.
* Централизованная обработка ошибок со стандартными HTTP-статусами.

---

### 1. Поиск экземпляров растений

#### Назначение

Получить постраничный список экземпляров растений, доступных текущему пользователю в активном контексте организации.

#### Контракт

```http
GET /api/inventory/plants
```

### Query Parameters

```text
keyword          необязательный текстовый поиск
organization     необязательный контекст тенанта / корневой организации
unit             необязательный фильтр по подразделению или коллекционной единице
list             необязательный фильтр по списку
recursive        необязательный флаг поиска по вложенным подразделениям
filter           необязательные фасетные фильтры
page             параметр пагинации
size             параметр пагинации
sort             параметр сортировки
```

#### Response

```json
{
  "items": [
    {
      "id": "uuid",
      "displayName": "string",
      "taxon": "summary",
      "inventoryCode": "string",
      "status": "string",
      "location": "summary",
      "visibility": "string"
    }
  ],
  "page": {
    "number": 0,
    "size": 25,
    "totalElements": 0
  }
}
```

#### Безопасность

* Требуется аутентифицированный пользователь.
* Результат ограничивается tenant-контекстом, доступным текущему пользователю.
* Query specifications применяют tenant-фильтрацию до возврата данных.
* Filter expressions разбираются в allowlisted-критерии, а не выполняются как сырые динамические запросы.
* Пагинация и сортировка используют framework-level pageable parameters.

---

### 2. Получение деталей экземпляра растения

#### Назначение

Получить один экземпляр растения как цифровую запись реального растения в живой коллекции.

#### Контракт

```http
GET /api/inventory/plants/{plantId}
```

#### Response

```json
{
  "id": "uuid",
  "taxon": {
    "id": "uuid",
    "displayName": "string",
    "type": "species | cultivar | grex"
  },
  "inventory": {
    "accessionNumber": "string",
    "individualCode": "string",
    "status": "string"
  },
  "organization": "summary",
  "location": "summary",
  "photos": ["summary"],
  "customFields": {}
}
```

#### Безопасность

* Требуется аутентифицированный пользователь.
* Доступ проверяется по принадлежности растения тенанту и членству пользователя в организации.
* Внутренние поля не раскрываются через публичные контракты.
* Несуществующие или недоступные ресурсы возвращаются через стандартные error responses.

---

### 3. Создание экземпляра растения

#### Назначение

Создать новый экземпляр растения в живой коллекции организации.

#### Контракт

```http
POST /api/inventory/plants
```

#### Request

```json
{
  "taxonId": "uuid",
  "organizationUnitId": "uuid",
  "placeId": "uuid",
  "inventoryData": {},
  "status": "string",
  "customFields": {}
}
```

#### Response

```http
201 Created
```

```json
{
  "id": "uuid",
  "displayName": "string",
  "taxon": "summary",
  "inventoryCode": "string",
  "status": "string"
}
```

#### Безопасность

* Требуется аутентифицированный пользователь.
* Требуется административный или редакторский доступ к целевому подразделению организации.
* Request body валидируется до выполнения доменной логики.
* `taxonId` обязателен и должен ссылаться на разрешённый вид, культивар или грекс, видимый в текущем tenant-контексте.
* Создание передаётся в service layer после авторизации и валидации.

---

### 4. Обновление экземпляра растения

#### Назначение

Обновить существующий экземпляр растения: инвентарные данные, таксономическую привязку, статус или организационное размещение.

#### Контракт

```http
PUT /api/inventory/plants/{plantId}
```

#### Request

```json
{
  "taxonId": "uuid",
  "organizationUnitId": "uuid",
  "placeId": "uuid",
  "inventoryData": {},
  "status": "string",
  "customFields": {}
}
```

#### Response

```json
{
  "id": "uuid",
  "displayName": "string",
  "taxon": "summary",
  "status": "string",
  "location": "summary"
}
```

#### Безопасность

* Требуется аутентифицированный пользователь.
* Требуется write access к существующей записи растения.
* Если растение перемещается в другое подразделение, должен быть проверен доступ и к текущему, и к целевому контексту.
* Недопустимые попытки перемещения отклоняются с ошибкой доступа.
* Валидация запроса выполняется через типизированные request DTO и Bean Validation.

---

### 5. Soft Delete экземпляра растения

#### Назначение

Переместить запись растения в корзину без физического удаления из базы данных.

#### Контракт

```http
DELETE /api/inventory/plants/{plantId}
```

#### Response

```http
204 No Content
```

#### Безопасность

* Требуется аутентифицированный пользователь.
* Требуется административный доступ к организационному контексту растения.
* Удаление по умолчанию является обратимым.
* Soft-deleted записи исключаются из обычных запросов.
* Permanent delete ограничен повышенными platform-level ролями.

---

### 6. Массовые операции с экземплярами растений

#### Назначение

Выполнить массовые действия над выбранными экземплярами растений: перемещение, обновление, клонирование, генерация данных для этикеток или отметка этикеток как напечатанных.

### Контракты

```http
POST /api/inventory/plants/batch/move
POST /api/inventory/plants/batch/update
POST /api/inventory/plants/batch/clone
POST /api/inventory/plants/batch/label-data
POST /api/inventory/plants/batch/mark-printed
```

#### Request

```json
{
  "plantIds": ["uuid"],
  "operationPayload": {}
}
```

#### Response

```json
{
  "successCount": 0,
  "failureCount": 0,
  "results": [
    {
      "id": "uuid",
      "status": "success | failed",
      "message": "string"
    }
  ]
}
```

#### Безопасность

* Требуется аутентифицированный пользователь.
* Каждое затронутое растение должно быть проверено на tenant ownership и права пользователя.
* Batch operations не должны обходить per-resource authorization.
* Для операций, где часть записей может не пройти валидацию или авторизацию, поддерживается partial success.
* Входные коллекции валидируются до обработки.

---

### 7. Получение справочников для форм растений

#### Назначение

Вернуть контролируемые справочные значения, используемые в формах растений: жизненные статусы, условия выращивания, формы поступления и другие значения.

#### Контракт

```http
GET /api/inventory/dictionaries/{dictionaryType}
```

#### Response

```json
[
  {
    "id": "string",
    "code": "string",
    "label": "string"
  }
]
```

#### Безопасность

* Для внутренних справочников требуется аутентифицированный пользователь.
* Ответы справочников содержат только безопасные reference data.
* Значения контролируются платформой или tenant-конфигурацией, а не произвольным free text.

---

### 8. Поиск таксона

#### Назначение

Предоставить единый поиск по видам, культиварам и грексам при создании или редактировании экземпляра растения.

#### Контракт

```http
GET /api/taxonomy/search
```

#### Query Parameters

```text
query       поисковая строка
type        необязательный фильтр по типу таксона
page        параметр пагинации
size        параметр пагинации
```

#### Response

```json
{
  "items": [
    {
      "id": "uuid",
      "displayName": "string",
      "taxonType": "species | cultivar | grex",
      "source": "reference | global | local"
    }
  ]
}
```

#### Безопасность

* Глобальные reference species доступны всем тенантам.
* Глобальные cultivated entities доступны всем тенантам.
* Локальные cultivated entities видимы только разрешённым tenant-контекстам.
* API скрывает внутреннюю механику видимости и отдаёт только selectable taxon summaries.

---

### 9. Workflow умного импорта

#### Назначение

Импортировать существующие коллекционные данные из таблиц через staged workflow.

#### Контракты

```http
POST /api/import/sessions
POST /api/import/sessions/{sessionId}/sheet
POST /api/import/sessions/{sessionId}/mapping
POST /api/import/sessions/{sessionId}/resolve
POST /api/import/sessions/{sessionId}/execute
GET  /api/import/sessions/{sessionId}/status
GET  /api/import/sessions/{sessionId}/error-report
```

#### Workflow

```text
Загрузка файла
→ Выбор листа
→ Сопоставление столбцов
→ Разрешение значений
→ Подтверждение неоднозначных совпадений
→ Выполнение импорта
→ Просмотр результатов
```

#### Response Example

```json
{
  "sessionId": "uuid",
  "status": "uploaded | mapped | resolving | ready | executing | completed | failed",
  "progress": {
    "processedRows": 0,
    "totalRows": 0
  }
}
```

#### Безопасность

* Требуется аутентифицированный пользователь.
* Требуется tenant-контекст и permission на импорт.
* Загруженные файлы хранятся вне реляционной базы данных.
* Import sessions являются tenant-scoped.
* Неоднозначные совпадения требуют подтверждения пользователя.
* Некорректные строки отражаются в отчёте, но не блокируют все валидные строки.
* Для долгих этапов импорта используются background jobs.

---

### 10. Публичная страница растения

#### Назначение

Предоставить безопасное публичное представление записи растения, обычно используемое как цель QR-этикетки.

#### Контракт

```http
GET /api/public/plants/{publicSlug}
```

#### Response

```json
{
  "displayName": "string",
  "taxon": "public summary",
  "organization": "public summary",
  "photos": ["public media reference"],
  "publicDescription": "string"
}
```

#### Безопасность

* Аутентификация не требуется.
* Возвращаются только public DTO.
* Исключаются внутренние идентификаторы, tenant metadata, приватные заметки, внутренние инвентарные поля и закрытые фотографии.
* Требуются публичные настройки видимости у организации-владельца и контекста растения / списка.
* Доступ к медиа использует short-lived signed URLs или эквивалентный контролируемый механизм доставки.

---

### 11. Поиск совпадений для обмена

#### Назначение

Найти потенциальные совпадения между wishlist одной организации и exchange lists других организаций.

#### Контракт

```http
GET /api/exchange/matches/{wishlistId}
```

#### Response

```json
{
  "wishlist": "summary",
  "matches": [
    {
      "taxon": "summary",
      "sourceOrganization": "public or shared summary",
      "availableMaterial": "summary",
      "visibility": "string"
    }
  ]
}
```

#### Безопасность

* Требуется аутентифицированный пользователь.
* Пользователь должен иметь доступ к исходному wishlist.
* Candidate matches ограничены данными, явно расшаренными для обмена или видимыми в соответствующем community scope.
* Matching основан на taxon identifiers, а не на raw text names.
* Private collection data не раскрывается через exchange API.

---

### Паттерн обработки ошибок

```json
{
  "status": 400,
  "code": "VALIDATION_ERROR",
  "message": "Request validation failed",
  "details": []
}
```

Типовые HTTP-статусы:

```text
200 OK                  успешное чтение или обновление
201 Created             ресурс создан
204 No Content          успешное удаление
400 Bad Request         некорректный ввод или ошибка доменной валидации
403 Forbidden           пользователь аутентифицирован, но доступ запрещён
404 Not Found           ресурс отсутствует или не видим пользователю
409 Conflict            конфликт состояния или ресурс используется
429 Too Many Requests   превышен rate limit
```

---

### Summary по безопасности

API-дизайн сочетает framework-level и domain-level protection:

* Spring Security аутентифицирует запросы и формирует user context.
* JWT несёт идентичность, а роли и membership’ы резолвятся на серверной стороне.
* Method-level checks защищают write-операции и административные действия.
* Tenant-scoped queries предотвращают утечку данных между организациями.
* DTO validation блокирует некорректные запросы до выполнения бизнес-логики.
* Public endpoints используют отдельные response models с ограниченным набором полей.
* Soft delete защищает от случайной потери данных.
* Platform-level operations отделены от tenant-level workflows.
* Audit и login events обеспечивают traceability для чувствительных действий.
