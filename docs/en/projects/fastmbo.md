# FastMBO - Internal Goal-Setting and Bonus Calculation System

**Type:** Internal automation / MBO system / lightweight internal ERP  
**Role:** initiator, systems analyst, concept author, prototype developer  
**Status:** historical internal project / reconstructed case study  
**Scale:** internal use in an organization of up to 350 employees  
**Period:** early transition stage from IT administration to systems analysis and internal systems development

## Overview

FastMBO is an internal system for automating goal-setting, evaluation sheet collection, achievement approval, and bonus calculation based on the MBO model.

The project emerged from a real operational pain point: employee evaluation was handled manually through paper forms, Excel files, repeated checks, manual digitization, and transfer of final results into accounting systems.

The idea was to replace a fragile manual process with a small internal ERP-like system: employees fill in evaluation sheets online, managers approve achievements, responsible users manage evaluation periods, and the system calculates scores, point value, and final bonuses.

## Context and Problem

Before automation, the process was heavily dependent on manual coordination:

- evaluation sheets were prepared and distributed manually;
- employees filled in paper forms;
- managers validated achievements and metrics;
- changes led to repeated approvals and reprints;
- scores were transferred to Excel;
- bonuses were calculated manually;
- final data was passed to the HR/accounting process.

Main problems:

- high effort required to prepare and process evaluation sheets;
- risk of errors during data transfer;
- difficulty tracking completion and approval statuses;
- no unified digital history by evaluation period;
- low transparency for process participants;
- dependency on specific employees who knew the manual calculation procedure.

## Project Goal and Requirements

Create an internal system that moves the MBO process from manual document flow to a controlled digital workflow.

The system was intended to support:

- creation and configuration of evaluation periods;
- management of metrics and achievement templates;
- generation of evaluation sheets for employees;
- online data entry;
- approval of achievements and metrics;
- automatic calculation of total scores, point value, and bonus amount;
- manual corrections where required;
- publication of results in a personal account;
- export of final results for further processing.

## Role and Contribution

In this project, I acted as a proactive systems analyst and internal developer.

My contribution:

- identified a recurring operational problem and proposed automation;
- formulated the concept of an internal MBO system;
- analyzed the AS-IS process and proposed a TO-BE process;
- collected and clarified requirements from future users;
- identified key roles, entities, statuses, and process stages;
- designed the domain model and high-level architecture;
- started independent implementation as a Java/Spring application;
- later reconstructed BPMN, C4, ERD, ADR, and economic justification materials for the portfolio.

## Target TO-BE Process

The target process assumed a transition to a controlled digital cycle:

1. Preparation of the evaluation period.
2. Approval of metrics and achievement templates.
3. Generation of evaluation sheets and assignment to job positions.
4. Period launch and input unlocking.
5. Online entry of metrics and achievements by employees.
6. Parallel validation by managers.
7. Period closure and input locking.
8. Automatic calculation of scores, point value, and bonuses.
9. Manual corrections where required.
10. Final approval.
11. Publication of bonuses in the personal account.
12. Export of final results to 1C via CSV or connector.

## Economic Effect

The project was justified through the reduction of manual work during preparation, checking, recalculation, and data transfer.

The estimate showed time savings of more than 300,000 RUB per year for an annual evaluation cycle. With a monthly or more frequent cycle, the effect scaled significantly due to process repetition.

Additional effect:

- less manual data transfer;
- fewer repeated approvals caused by corrections;
- higher status transparency;
- faster preparation of final results;
- easier audit of the evaluation period.

## User Roles

- **Employee** - fills in the evaluation sheet, adds achievements, views results.
- **Manager** - approves achievements and metrics of direct reports.
- **Responsible user** - controls the period and checks data completeness and correctness.
- **Director** - approves final results and controls the bonus fund.
- **System administrator** - manages settings, users, periods, and audit.

## Architectural Approach

The system was designed as a monolithic web application for internal use.

A monolith was justified by the context:

- limited user base;
- internal deployment;
- one main business process;
- no need for distributed architecture;
- limited maintenance resources.

The target architecture included:

- web interface for employees and managers;
- authentication and authorization;
- service layer for business logic;
- relational storage;
- reporting and export module;
- action logging;
- file storage for attachments.

## Architecture Artifacts

### BPMN Business Processes

#### AS-IS

![AS-IS BPMN](https://flatura.github.io/fastmbo_docs/docs/bpmn/as-is.svg)

#### TO-BE

![TO-BE BPMN](https://flatura.github.io/fastmbo_docs/docs/bpmn/to-be.svg)

### C4 Context

![C4 Context](https://flatura.github.io/fastmbo_docs/docs/uml/c4_context.svg)

### C4 Container

![C4 Container](https://flatura.github.io/fastmbo_docs/docs/uml/c4_container.svg)

### C4 Component

![C4 Component](https://flatura.github.io/fastmbo_docs/docs/uml/c4_component.svg)

### ERD

![ERD](https://raw.githubusercontent.com/flatura/fastmbo_docs/master/docs/uml/erd.svg)

### ADR

[Architecture Decision Records](fastmbo-adr.md)

## Project Limitations

The project was not brought to the maturity level of a production system with a full delivery lifecycle, testing process, release process, and ongoing support.

The original documentation was incomplete and insufficiently formalized. Part of the current architecture materials was reconstructed later as a portfolio case study.

## What This Project Demonstrates

FastMBO demonstrates an early stage of my professional evolution: from an infrastructure-focused role to systems analysis, internal automation, and architectural thinking.

The project demonstrates:

- ability to identify an operational problem and propose automation;
- transition from a manual process to a digital workflow;
- work with roles, statuses, periods, calculations, and approvals;
- understanding of the economic effect of automation;
- early experience designing an internal ERP-like system;
- transition from “writing a utility” to “designing a system”.

## Full Documentation

- Documentation repository: <https://github.com/flatura/fastmbo_docs>