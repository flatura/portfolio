# Дорожная карта и демонстрация

## Дорожная карта

| Фаза | Цель | Exit criteria |
|---|---|---|
| v0.1 Lab PoC | Показать controlled LLM execution | Запрос → диагностический путь → вызовы tools → ответ + run details. ПРОТОТИПИРОВАНО |
| v0.2 Стабилизированный запуск | Стабилизировать один финансовый и один операционный сценарий | Демо проходит без ручной подмены результата. ПРОТОТИПИРОВАНО |
| v0.3 Документальный доказательный слой | Усилить evidence через RAG | Ответ может ссылаться на документы/чанки. ПРОТОТИПИРОВАНО как направление |
| v0.4 Tool Registry v0.1 | Увести захардкоженные инструменты в сторону registry | Инструменты описаны через манифест; отдельный tool-server. ПРОТОТИПИРОВАНО как начальный концепт |
| v0.5 Исполнительный отчет | Перейти от chat answer к report artifact | Executive brief + signal cards + evidence appendix. НЕ РЕАЛИЗОВАНО |
| v0.6 Cross-domain scenario | Показать цепочку finance → delivery → ITSM → PMO | Прототип может исследовать заложенную кросс-доменную причину. ИССЛЕДОВАНО, НЕ ПОЛНОСТЬЮ СТАБИЛИЗИРОВАНО |
| v1 Настоящий MVP | См. ниже | Не достигнуто |

## Следующий шаг к MVP

Чтобы стать настоящим MVP, прототипу потребовались бы:

1. multi-turn session state;
2. корректная обработка уточняющих вопросов;
3. продолжение того же аналитического run;
4. persisted run/session context;
5. более формальная schema для tool registry;
6. evaluation harness;
7. read-only connectors к реалистичным enterprise data sources;
8. authentication and authorization model;
9. audit and observability layer;
10. demo-сценарии с measurable expected outcomes.

Текущая работа — technical PoC / рабочий прототип. Это ещё не настоящий MVP.

## Demo-сценарии

Сценарии ниже — это single-turn аналитические запросы на синтетических данных. Они показывают intended flow, а не законченный conversational product.

### Сценарий 1. Финансовая диагностика

Пример вопроса:

```text
Почему в марте 2025 просела валовая маржа?
```

Ожидаемый flow прототипа: направить вопрос в финансовый диагностический путь, вызвать metric tools для gross margin, revenue, discounts, COGS и product mix, затем сформировать структурированное резюме с evidence и ограничениями.

### Сценарий 2. Операционная диагностика

Пример вопроса:

```text
Почему time-to-market нестабилен, хотя локальные KPI команд выглядят нормально?
```

Ожидаемый flow прототипа: направить вопрос в операционный диагностический путь и посмотреть delivery, PMO, ITSM, решения встреч и связанные evidence на кросс-функциональные узкие места, которые плохо видны в изолированных KPI-дашбордах.

### Сценарий 3. Кросс-доменная диагностика

Целевой вопрос:

```text
Почему во втором квартале просела маржа online-канала, если продажи и локальные KPI digital-команд выглядели нормально?
```

Целевая диагностическая цепочка:

```text
маржа ↓
-> скидочное давление ↑
-> задержка промо-сегментации
-> rework в delivery
-> инциденты stock availability integration
-> PMO status green illusion
-> решение по DoR не стало action item
-> управленческий вывод с evidence trail
```

Статус: целевой demo-flow; исследован, но требует стабилизации cross-domain linkage и качества evidence.

## Скриншоты и демо

### «Что ты умеешь?»

<figure markdown>
![UI_1](/portfolio/assets/ai_oip/what.png)
<figcaption>Прототипный каталог диагностических путей и tools</figcaption>
</figure>

### Финансовый диагностический путь: гипотеза о падении валовой маржи

<figure markdown>
![UI_2](/portfolio/assets/ai_oip/gross_margin.png)
<figcaption>Диагностика финансовых показателей: гипотеза падения маржи</figcaption>
</figure>

<figure markdown>
![UI_3](/portfolio/assets/ai_oip/gross_margin_report.png)
<figcaption>Диагностика финансовых показателей: отчёт об использовании</figcaption>
</figure>

<figure markdown>
![UI_4](/portfolio/assets/ai_oip/tools_called.png)
<figcaption>Диагностика финансовых показателей: вызванные инструменты и run details</figcaption>
</figure>

### Операционный диагностический путь: аномалии KPI

<figure markdown>
![UI_5](/portfolio/assets/ai_oip/KPI.png)
<figcaption>Диагностика операционных аномалий на стыке delivery, ITSM, PMO и документов</figcaption>
</figure>

## Что демонстрирует проект

Проект показывает способность взять неоднозначную enterprise AI-идею и превратить её в ограниченный, демонстрируемый прототип.

Он демонстрирует:

- понимание рисков enterprise AI;
- controlled LLM execution вместо свободного чата;
- разделение chat UI и execution layer;
- tool-mediated analytics;
- evidence-backed response design;
- execution trace как механизм доверия и отладки;
- способность быстро собрать working prototype;
- способность честно документировать ограничения.

Главная ценность — не «использование LLM». Главная ценность — проектирование системы, где AI-рассуждение ограничено архитектурой, evidence, контрактами инструментов и аудируемостью, и явное описание того, что прототип реализовал, а чего не реализовал.
