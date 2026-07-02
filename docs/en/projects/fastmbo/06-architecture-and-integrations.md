# Architecture and Integrations

## Architecture

## Architectural Approach

The system was designed as a monolithic web application for internal use.

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

## Integration Flows

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
