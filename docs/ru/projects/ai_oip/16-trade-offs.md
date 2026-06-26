# Компромиссы

## Lab runtime отделён от целевой архитектуры

LangGraph и Open WebUI используются как быстрые MVP/lab tools. Целевая продуктовая архитектура предполагает backend-native control plane, dedicated UI, Tool Gateway, semantic layer, report service и audit trail.

## Open WebUI как временный интерфейс

Настроил Open WebUI как временный chat-интерфейс для демонстрации MVP вместо создания dedicated executive UI на старте.
