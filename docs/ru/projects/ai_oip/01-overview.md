# Обзор

## Обзор прототипа

**AI Operational Intelligence Prototype** — технический прототип управляемого LLM-контура для аналитики на проверяемых данных.

Исходное рабочее название — AI Operational Intelligence Platform / Executive Decision Intelligence. Оно описывало целевое продуктовое направление, а не зрелость реализованного результата.

Прототип проверяет подход к построению управленческой AI-аналитики. Пользователь задаёт аналитический вопрос в chat-like интерфейсе; backend запускает контролируемый execution flow по подготовленным синтетическим данным. LLM должна работать внутри backend-mediated tool environment, а не как свободный чат-бот с произвольным доступом к данным.

Это не production-платформа и не законченный multi-turn продукт поддержки принятия решений. Это экспериментальный прототип enterprise AI-архитектуры, который проверял ограниченную идею управляемого выполнения.

## Что было прототипировано

- chat-like интерфейс на базе Open WebUI;
- экспериментальный LangGraph-based execution flow;
- backend tools для обращения к подготовленным синтетическим данным;
- начальный tool registry / концепт описания доступных инструментов;
- синтетические финансовые и кросс-функциональные управленческие сценарии;
- single-turn аналитические запросы;
- паттерн evidence-backed responses;
- базовая трассировка выполнения / run details;
- архитектурная документация и направление развития.

## Технологический стек

| Слой | Решение в PoC | Назначение |
|---|---|---|
| Chat-like UI | Open WebUI | Временный интерфейс для демонстрации |
| Execution flow | FastAPI + LangGraph | Экспериментальный single-request диагностический flow |
| Tool execution | FastAPI tool-server | Контролируемые backend tools, валидация, структурированный вывод |
| Структурированные данные | PostgreSQL | Синтетические finance, delivery, ITSM, PMO, meetings данные |
| Документное хранилище | MinIO + Qdrant | Направление document evidence для RAG |
| Runtime/cache | Redis | Поддержка лабораторного runtime |
| LLM | OpenAI-совместимое API | Планирование и синтез; не источник истины |
| Infra | Docker Compose | Воспроизводимый лабораторный стенд |

**Исследованные архитектурные паттерны:** Tool Gateway, концепт Tool Registry, прототип playbook-routing, направление RAG, run trace, evidence trail.

**Подход к разработке:** AI-assisted prototyping, генерация синтетических данных, scenario-driven проверка PoC.
