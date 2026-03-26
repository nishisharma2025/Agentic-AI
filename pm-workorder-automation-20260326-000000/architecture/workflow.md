# Workflow Diagram

``mmarid
\lowchart TD\n    A[Asset Created] --> B[PM Schedule Triggered]
    B --> C[Work Order Generated]
    C --> D[Assigned to Technician]
    D --> E[Work Execution]
    E --> F[Quality Check]
    F --> G[Work Order Closed]
```