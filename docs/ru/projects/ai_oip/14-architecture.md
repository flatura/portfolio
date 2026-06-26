# Архитектура

## Tool Gateway pattern

Весь доступ к данным проходит через controlled HTTP tools с явными input contracts, validation, structured output и metadata.

## Playbook-based diagnostics

Система маршрутизирует вопросы в доменные diagnostic playbooks вместо того, чтобы раскрывать LLM все tools сразу.

Каждый бизнес-домен раскрывает ограниченный набор разрешённых tools, диагностических шагов, ограничений и ожидаемых evidence.

## Tool Registry

Реализовал и развил концепцию Tool Registry как machine-readable каталога доступных tools, схем, доменов, ограничений и разрешённых playbooks.
