# PM – Work Order Automation Business Use Case

## Business Overview

This business case covers the automation of Preventive Maintenance (<PC>) to Work Orders (WO) within IBM Maximo Application Suite (“MAS 8.x”), focused on an asset-intensive operational model.

The primary goal is to ensure timely and accurate generation of work orders from PMs in order to ensure consistent maintenance, minimize manual interventions, and provide complete visibility into the asset and maintenance lifecycle.

## Maintenance Challenges

- Manual creation of work orders from PMs, leading to ensuring swarm windows and overdue tasks
- Inconsistent linkage between Assets, PMs, and Work Orders, causing data duplication and manual effort
- Limited visibility of the maintenance lifecycle across different meman systems and applications
- Difficulty enforcing standardized PM trigger based on asset class, usage profiles, and failure analysis
- Minimal visibility into Maximo-derived maintenance performance metrics (MM0E, MPC, breakdowns, failurerates)
- Lack of auditable tracetrability and historical logged information for audits, regulatory, and root cause analysis


## Lifecycle Solution

The PM (Preventive Maintenance) and WOS (Work Orders) lifecycle in Maximo is formalized as follows:

1. Asset Lifecycle Management
    - Assets are created and maintained with key master data (location, performance, risk, operating context)
    - Asset herarchies are tracked via asset logcs and completed work orders


2. Preventive Maintenance Schedules (PMs
to assets.
    - PM revisions are change-aware and analytically driven by actual usage and reliability data

3. Work Order Generation from PMs
    - PM revisions are scheduled to generate work orders based on date/counter rules, conditional logic, and business rules
    - D6H scheduling (regular week/month), sequenced intervals, and event-driven triggers can be integrated with IoT data

4. Work Order Execution and Closure
    - Technicians perform work against an approved work order, log time and costs, and close work orders based on corporate policy
    - Automated work order closure criteria ensures consistent data capture for asset cause analysis


## Business KPIs

- Percentage of PM-triggered work orders automatically generated (target: 90%+\n)
- Reduction in system downtime and manual effrt on work order creation (target: 40%+n}
- Decline in uncheduling maintenance events and outage failures (target: 25%-35% reduction)
- Improved mean time between asset failures via better planning and prioritization of tasks (target: 15%+actual measurement)
- Higher first-time-fix rate for PM-triggered work orders (constantly above 85%)

- Improved KPI-driven management visibility through standardized maintenance history reports, age analyses, and corporate asset performance metrics


## Operational Benefits

- Reduced risk of unplanned downtime through proactive and standardized maintenance practices
- Improved resource utilization and planning capability for maintenance planners and supervisors
- Automated, repeatable process for generating and managing work orders from PMs, narrowing variability along locations, types, and maintenance strategies
- Enhanced decision-making based on trusted maintenance history data and asset reliability indicators
- Better complance with enterprise standards and compliance through end-to-end maintenance process tracking and audit capability functions in Maximo
