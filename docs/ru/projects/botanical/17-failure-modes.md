# Режимы отказа

| Риск                    | Последствие                 | Митигирующая мера                           |
| ----------------------- | --------------------------- | ------------------------------------------- |
| ошибка tenant filtering | утечка данных               | тесты, AccessControlService, scoped queries |
| падение VPS             | недоступность сервиса       | backup, restore plan, migration path        |
| потеря MinIO volume     | потеря фото/импортов        | object storage backup                       |
| зависший import job     | блокировка импорта          | job lifecycle, stale detection              |
| public DTO leakage      | раскрытие внутренних данных | отдельные DTO, visibility rules             |
