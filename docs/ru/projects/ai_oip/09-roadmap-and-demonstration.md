# Дорожная карта и демонстрация
## Дорожная карта

| Фаза | Цель | Exit criteria |
|---|---|---|
| v0.1 Lab PoC | Показать контролируемую работу с LLM | Вопрос -> плейбук -> вызов инструментов -> ответ + детали запуска. РЕАЛИЗОВАНО |
| v0.2 Стабилизированный запуск | Стабилизировать один финансовый и один операционный сценарий | Демо проходит без ручной подмены результата. РЕАЛИЗОВАНО |
| v0.3 Документальный доказательный слой | Усилить доказательство чере RAG | Ответ ссылается на документы, чанки. РЕАЛИЗОВАНО |
| v0.4 Tool Registry v0.1 | Убрать захардкоженные инструменты из промтов | Инструменты описаны через регистр/манифест, поднят отдельный сервер инструментов РЕАЛИЗОВАНО |
| v0.5 Исполнительный отчет | Перейти от chat answer к report artifact | Executive brief + signal cards + evidence appendix |
| v0.6 Cross-domain scenario | Показать finance -> delivery -> ITSM -> PMO цепочку | Система находит заложенную кросс-доменную причину. РЕАЛИЗОВАНО, СТАБИЛИЗИРУЕТСЯ |
| v1 Pilot candidate | Подготовить первый рабочий узкий демо-стеннд | PMO / ITSM / Готов полноценный диагностический сценарий.  |

## Demo-сценарии

### Сценарий 1. Финансовая диагностика

Пример вопроса:

```text
Почему в марте 2025 просела валовая маржа?
```

Ожидаемый flow:

1. Выбор Financial Operations Playbook.
2. Вызов `metric_gross_margin`.
3. Вызов `metric_revenue`, `metric_discount_rate`, `metric_cogs_rate`, `metric_product_mix`.
4. При необходимости - `rag_search` по финансовым документам.
5. Ответ: facts, interpretation, hypothesis, limitations, recommended actions.

### Сценарий 2. Операционная диагностика

Пример вопроса:

```text
Почему time-to-market нестабилен, хотя локальные KPI команд выглядят нормально?
```

Ожидаемый flow:

1. Выбор Executive Operations / Delivery-oriented Playbook.
2. Анализ delivery rework, roadmap slippage, ITSM impact, PMO status.
3. Поиск решений и протоколов через RAG.
4. Выявление cross-functional bottleneck.
5. Ответ с next management actions.

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

Статус: целевой сильный demo-flow; требует стабилизации cross-domain linkage и evidence quality.

## Скриншоты и демо

### “Что ты умеешь?”

<figure markdown>
![UI_1](/portfolio/assets/ai_oip/what.png)
<figcaption>Доступные playbooks и tools</figcaption>
</figure>

### Финансовый плейбук: гипотеза о падении валовой маржи

<figure markdown>
![UI_2](/portfolio/assets/ai_oip/gross_margin.png)
<figcaption>Диагностика финансовых показателей: гипотеза падения маржи</figcaption>
</figure>

<figure markdown>
![UI_3](/portfolio/assets/ai_oip/gross_margin_report.png)
<figcaption>Диагностика финансовых показателей: отчет о расходе токенов (пока в символах)</figcaption>
</figure>

<figure markdown>
![UI_4](/portfolio/assets/ai_oip/tools_called.png)
<figcaption>Диагностика финансовых показателей: ход размышлений и список вызванных инструментов</figcaption>
</figure>

### Операционный плейбук: аномалии системы целеполагания

<figure markdown>
![UI_5](/portfolio/assets/ai_oip/KPI.png)
<figcaption>Диагностика операционных аномалий на стыке delivery, ITSM, PMO и документов</figcaption>
</figure>