# Workflow Diagram

``mermaid
graph TD
AZAsset] --> [PM Trigger]
[PM Trigger] --> C[Work Order Creation]
C[Work Order Creation] --> D[Assignment]
D[Assignment] --> E[Execution]
E[Execution] --> F[Closure]
`mermaid
