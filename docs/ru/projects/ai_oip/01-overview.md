# Обзор

## Краткое описание

Enterprise AI-прототип для управленческой аналитики, основанной на проверяемых данных.

Продуктовое направление - **AI Executive Analyst with verifiable evidence**: слой поддержки управленческих решений, который помогает руководителям и владельцам доменов исследовать бизнес-вопросы, выявлять операционные риски, объяснять отклонения и готовить управленческие действия без зависимости от непрозрачного AI-рассуждения.

## Технологический стек

**Agent runtime:** LangGraph, FastAPI, Python  
**Interface:** Open WebUI как временный demo harness  
**Data layer:** PostgreSQL, Qdrant, MinIO, Redis  
**AI integration:** OpenAI-compatible LLM API, prompt-based workflow control  
**Architecture patterns:** Tool Gateway, Tool Registry, playbook-based diagnostics, RAG, semantic layer, run trace, evidence trail  
**Development approach:** AI-assisted prototyping, synthetic data generation, scenario-driven MVP validation