RU:

## AI Executive Decision Intelligence / Agent Harness Prototype

**Тип:** Enterprise AI / Decision-support system / Agentic analytics prototype
**Роль:** System Designer, AI-assisted Prototype Engineer
**Статус:** рабочий прототип, May 2026

### Контекст

Прототип системы для управленческой аналитики, где LLM не “отвечает из головы”, а работает внутри контролируемого исполнительного контура: выбирает разрешённые инструменты, вызывает backend-функции, получает проверяемые данные, сохраняет трассу выполнения и формирует executive-level ответ на основе evidence.

### Зона ответственности

* Спроектировал общий контур AI Executive Decision Intelligence.
* Собрал LangGraph-based agent harness для управляемого выполнения сценариев.
* Выделил отдельный tool registry для описания доступных инструментов и ограничений.
* Подготовил синтетические финансовые и кросс-функциональные управленческие сценарии.
* Настроил Open WebUI как chat-like интерфейс для демонстрации PoC.
* Проработал подход к traceability: tool calls, параметры, результаты, run-level evidence.
* Сформировал направление развития: playbooks, evidence graph, report generation, tool generator.

### Ключевые решения

* Controlled LLM execution вместо свободного chat-подхода.
* Tool registry как граница между LLM и backend-возможностями.
* Evidence-backed answers: ответ должен ссылаться на данные, а не только на рассуждение модели.
* Run trace как основа доверия, отладки и аудита.
* Разделение ролей: backend задаёт рамки, LLM действует внутри ограниченного сценария.

## Скриншоты решения
### "Что ты умеешь?"
<figure markdown>
![UI_1](assets/ai_oip/what.png)
<figcaption>"Что ты умеешь?"</figcaption>
</figure>

### Финансовый плейбук: причина падения маржи
<figure markdown>
![UI_1](assets/ai_oip/gross_margin.png)
<figcaption>Гипотеза: причина падения маржи</figcaption>
</figure>

### Кроссфункциональный плейбук: аномалии системы целеполагания
<figure markdown>
![UI_1](assets/ai_oip/KPI.png)
<figcaption>Аномалия системы целеполагания</figcaption>
</figure>


### Технологический стек

LangGraph, Python, Open WebUI, synthetic datasets, tool registry, agent harness, LLM-assisted development, evidence-based analytics.

### Что показывает проект

Этот проект показывает мой переход от классического системного анализа к проектированию enterprise AI-систем: собрать контролируемый контур, где есть инструменты, ограничения, трассировка, проверяемые данные и понятная управленческая ценность.
