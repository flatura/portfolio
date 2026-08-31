# Безопасность, качество и эксплуатация

## Модель безопасности и доступа

### Реализовано в PoC

- Используются только synthetic data.
- LLM не получает прямой доступ к PostgreSQL, Qdrant и MinIO.
- Доступ к данным идёт через controlled HTTP tools.
- Tools имеют явные input contracts.
- Финансовые расчёты выполняются named queries / backend logic, а не произвольным SQL от LLM.
- В run details видны выбранный диагностический путь, tool calls, inputs и outputs.

### Целевая production-модель — не реализована

- SSO / IdP integration.
- RBAC / ABAC.
- Tenant isolation.
- ACL-aware RAG retrieval.
- Tool permissions by diagnostic path, user role and domain.
- Read-only mode по умолчанию.
- Approval gates для write-действий.
- Full audit log: run_id, user_id, tool_id, params hash, result hash, source refs.
- Secrets management.
- On-prem/private deployment option.

## Controlled LLM execution

LLM может планировать следующий шаг, но доступ к данным делегирован контролируемым backend tools — не свободному чату над корпоративными данными.

## Модель контролируемого доступа к инструментам

LLM никогда не обращается к PostgreSQL, Qdrant или MinIO напрямую.

## Нефункциональные требования

PoC не оценивался и не доказывался против production NFR. Значимые лабораторные ограничения:

- демонстрируемый single-request flow;
- трассируемость вызовов инструментов;
- отсутствие прямого доступа модели к хранилищам данных;
- воспроизводимый стенд на Docker Compose;
- только синтетические данные.

## Режимы отказа

| Failure mode | Проявление | Комментарий |
|---|---|---|
| Неверный routing диагностического пути | Операционный вопрос мог уйти в finance path | Уточнение исследовалось, но ответ пользователя не продолжал ту же сессию |
| Unsupported question | Вопрос вне покрытия dataset/tools | Явное limitation предпочтительнее выдуманного ответа |
| Duplicate tool calls | Agent вызывает один и тот же tool с теми же параметрами | Fingerprint `tool_id + canonical_json(args)`, run-local cache |
| Stub/empty tool response | Tool не вернул данные или вернул заглушку | Status handling, warning, insufficient evidence verdict |
| Missing RAG evidence | Документальный слой не находит подтверждения | Явное limitation: document evidence not found |
| Hallucinated conclusion | LLM формулирует вывод без evidence | Evidence-first prompt; evaluation pipeline не реализован |
| Incomplete cross-domain linkage | Метрики есть, но связь finance ↔ delivery ↔ ITSM не доказана | Нужен более сильный semantic layer; не полностью стабилизировано |
| External LLM unavailable | API недоступен или лимитирован | Retry/backoff и local-model option — будущая работа |
| Context overflow | Tool manifest/evidence слишком велики | Context budget, summarization, retrieval filters — ранняя стадия |
| Data leakage risk | Модель видит лишние данные | Tool-level permissions и no direct data access; production ACL нет |

## Оценка масштаба и стоимости

Текущий PoC рассчитан на демонстрационный режим:

- 1-3 одновременных пользователя;
- единицы diagnostic runs во время демо;
- synthetic dataset за период 2024-2025;
- десятки/сотни тысяч строк максимум в рамках lab-данных;
- один run обычно должен укладываться в 1-10 tool calls;
- стоимость определяется LLM API calls и инфраструктурой Docker/VPS/local machine;
- production sizing не выполнялся.

Для production потребуются отдельные оценки объёма источников, размера document corpus, частоты ingestion, числа пользователей, RPS, SLA, стоимости LLM routing и требований к private deployment. Эта работа не выполнялась.
