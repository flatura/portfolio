# Архитектура и интеграции

## Архитектура

## Tool Gateway pattern

Весь доступ к данным проходит через controlled HTTP tools с явными input contracts, validation, structured output и metadata.

## Playbook-based diagnostics

Система маршрутизирует вопросы в доменные diagnostic playbooks вместо того, чтобы раскрывать LLM все tools сразу.

Каждый бизнес-домен раскрывает ограниченный набор разрешённых tools, диагностических шагов, ограничений и ожидаемых evidence.

## Tool Registry

Реализовал и развил концепцию Tool Registry как machine-readable каталога доступных tools, схем, доменов, ограничений и разрешённых playbooks.

## Потоки интеграции

## Evidence-first answers

Финальные ответы должны опираться на tool outputs, document evidence, calculations или явно обозначенные limitations.

## Run trace как слой доверия

Каждый diagnostic run сохраняет selected playbook, tool calls, parameters, outputs и reasoning checkpoints для debugging и audit.

## Подход к evidence и прозрачности

Разработал подход к evidence и прозрачности: selected playbook, tool calls, parameters, tool results, execution timeline, run details и JSON-level debug visibility.
