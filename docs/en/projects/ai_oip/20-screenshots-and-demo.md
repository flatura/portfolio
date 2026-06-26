# Screenshots and Demo

## Demo Scenarios

### Financial Performance Diagnosis

Example question:

> Why did gross margin drop in March?

The system selects a financial diagnostic playbook, calls metric tools for gross margin, revenue, discounts, COGS, and product mix, then produces an executive summary with evidence and limitations.

### Operational / KPI Anomaly Diagnosis

Example question:

> Why is time-to-market unstable while local team KPIs look normal?

The system selects an operational diagnostic playbook and investigates delivery, PMO, ITSM, meeting decisions, and related evidence to detect cross-functional bottlenecks that are not visible in isolated KPI dashboards.

### Cross-Domain Management Hypothesis

Target scenario:

> Identify the top problematic projects, explain the selection criteria, describe the issue for each project, and prepare a meeting agenda for product owners.

This scenario demonstrates the intended product direction: not just retrieving delayed tasks, but turning structured and document evidence into a management-ready diagnostic brief.

## UI Screenshots

### "What can you do?"

<figure markdown>
![UI_1](/portfolio/assets/ai_oip/what.png)
<figcaption>Available playbooks and tools</figcaption>
</figure>

### Financial playbook: gross margin drop hypothesis

<figure markdown>
![UI_2](/portfolio/assets/ai_oip/gross_margin.png)
<figcaption>Financial performance diagnosis with tool-based evidence</figcaption>
</figure>

<figure markdown>
![UI_3](/portfolio/assets/ai_oip/gross_margin_report.png)
<figcaption>Financial performance diagnosis chars report</figcaption>
</figure>

<figure markdown>
![UI_4](/portfolio/assets/ai_oip/tools_called.png)
<figcaption>Financial performance diagnosis called tools</figcaption>
</figure>

### Executive Operations playbook: KPI anomaly

<figure markdown>
![UI_5](/portfolio/assets/ai_oip/KPI.png)
<figcaption>Operational anomaly diagnosis across delivery, ITSM, PMO, and documents</figcaption>
</figure>
