# Архитектура

## Архитектурный подход

Система проектировалась как монолитное веб-приложение для внутреннего использования.

Целевая архитектура включала:

- веб-интерфейс для сотрудников и руководителей;
- аутентификацию и авторизацию;
- сервисный слой бизнес-логики;
- реляционное хранилище;
- модуль отчётности и экспорта;
- журналирование действий;
- файловое хранилище для вложений.

## Архитектурные артефакты

### Бизнес-процессы BPMN

#### AS-IS

![AS-IS BPMN](https://flatura.github.io/fastmbo_docs/docs/bpmn/as-is.svg)

#### TO-BE

![TO-BE BPMN](https://flatura.github.io/fastmbo_docs/docs/bpmn/to-be.svg)

### C4 Context

![C4 Context](https://flatura.github.io/fastmbo_docs/docs/uml/c4_context.svg)

### C4 Container

![C4 Container](https://flatura.github.io/fastmbo_docs/docs/uml/c4_container.svg)

### C4 Component

![C4 Component](https://flatura.github.io/fastmbo_docs/docs/uml/c4_component.svg)
