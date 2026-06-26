# Модель безопасности и доступа

## Требования к доступу

- Необходимо обеспечить ограничение доступа к сервису.
- Необходимо обеспечить разделение пользовательских данных.

## Аутентификация - AWS Cognito

* **Разделение пользовательских данных:** AWS Cognito - встроенный менеджмент учётных записей, регистрация, 2FA, защита от брутфорса и т.п. Сервис бесшовно встроен в экосистему AWS.
* Проверка прав пользователя на файл при скачивании (`get_download_url` проверяет доступ в DynamoDB перед выдачей Presigned URL).

### Аутентификация

```mermaid
sequenceDiagram
    autonumber
    
    actor U as Браузер (SPA)
    participant API as API Gateway
    participant C as Amazon Cognito

    U->>API: Запрос к API (без JWT / протухший JWT)
    activate API
    API-->>U: 401 Unauthorized
    deactivate API
    U->>U: SPA очищает локальные данные
    U->>C: Редирект на Hosted UI форму логина
    activate C
    C->>U: Форма логина 
    deactivate C
    U->>C: Ввод данных и попытка аутентификации
    activate C
    alt Некорректные реквизиты
        C-->>U: Возврат ошибки (Invalid credentials)
    else Корректные реквизиты
        C-->>U: Возврат Auth Code (через redirect_uri)
        deactivate C
        U->>C: POST /oauth2/token (Обмен Code на JWT)
        activate C
        C-->>U: Access & ID Tokens
        deactivate C
    end
```
