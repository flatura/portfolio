# Безопасность, качество и эксплуатация

## Модель безопасности и доступа

### Реализовано в PoC

- Используются только synthetic data.
- LLM не получает прямой доступ к PostgreSQL, Qdrant и MinIO.
- Доступ к данным идёт через controlled HTTP tools.
- Tools имеют явные input contracts.
- Финансовые расчёты выполняются named queries / backend logic, а не произвольным SQL от LLM.
- В run details видны selected playbook, tool calls, inputs и outputs.

### Целевая production-модель

- SSO / IdP integration.
- RBAC / ABAC.
- Tenant isolation.
- ACL-aware RAG retrieval.
- Tool permissions by playbook, user role and domain.
- Read-only mode по умолчанию.
- Approval gates для write-действий.
- Full audit log: run_id, user_id, tool_id, params hash, result hash, source refs.
- Secrets management.
- On-prem/private deployment option.

## Режимы отказа

| Failure mode | Проявление | Смягчение |
|---|---|---|
| Wrong playbook routing | Операционный вопрос уходит в finance playbook | Intent confidence, no silent fallback, clarification flow |
| Unsupported question | Пользователь спрашивает вне покрытия dataset/tools | Ask user / explicit limitation вместо выдуманного ответа |
| Duplicate tool calls | Agent вызывает один и тот же tool с теми же параметрами | Fingerprint `tool_id + canonical_json(args)`, run-local cache |
| Stub/empty tool response | Tool не вернул данные или вернул заглушку | Status handling, warning, insufficient evidence verdict |
| Missing RAG evidence | Документальный слой не находит подтверждения | Явное limitation: document evidence not found |
| Hallucinated conclusion | LLM формулирует вывод без evidence | Evidence-first prompt, evaluator, claim-to-evidence policy |
| Incomplete cross-domain linkage | Метрики есть, но связь finance ↔ delivery ↔ ITSM не доказана | Graph/entity links, scenario truth, better semantic layer |
| External LLM unavailable | API недоступен или лимитирован | Retry/backoff, model gateway, local model option в будущем |
| Context overflow | Tool manifest/evidence слишком велики | Context budget telemetry, evidence summarization, retrieval filters |
| Data leakage risk | Модель видит лишние данные | Tool-level permissions, ACL filters, no direct data access |

## Оценка масштаба и стоимости

Текущий PoC рассчитан на демонстрационный режим:

- 1-3 одновременных пользователя;
- единицы diagnostic runs во время демо;
- synthetic dataset за период 2024-2025;
- десятки/сотни тысяч строк максимум в рамках lab-данных;
- один run обычно должен укладываться в 1-10 tool calls;
- стоимость определяется LLM API calls и инфраструктурой Docker/VPS/local machine;
- production sizing не выполнялся.

Для production потребуются отдельные оценки:

- объём подключаемых источников;
- размер document corpus;
- частота ingestion;
- число пользователей;
- RPS для chat/report API;
- SLA по daily reports;
- стоимость LLM routing;
- требования к on-prem/private deployment.
