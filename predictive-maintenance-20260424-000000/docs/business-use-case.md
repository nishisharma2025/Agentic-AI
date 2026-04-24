# Business Use Case: Predictive Maintenance with IoT Sensors

Scenario: A manufacturing company wants to implement predictive maintenance using IoT sensors. When a sensor detects abnormal vibration or temperature on a critical asset, it should automatically create a work order for inspection and possible corrective maintenance.

## 1. Business Context & Objectives

The company operates multiple manufacturing plants with critical rotating equipment (each worth $2-5M of capacity). Currently, maintenance is driven by planned preventive Maintenance (PM) schedules and reactive maintenance based on breakdowns.

These methods have limitations:
- Difficulty safely issues with critical assets crashing between scheduled checks
- Iraddic replacement of parts where the actual failure pattern would have allowed continued use
- Lack of visibility into real-time asset conditions and degree of wear (he atcual conditions is captured and analyzed only in incidental scenarios)

The company wants to use industrial IoT sensors (gate way vibration, temperature, trans&) connected to IBM Cloud/Edge and Maximo Application Suite (MAS Manage) to implement predictive maintenance that automatically creates work orders when anomalies are detected.

Primary objectives: 
- Reduce unplanned 'breakfown' down time and emergency maintenance on critical assets
- Improve meantime response to early warnings of failing components
- Improve asset availability and extend life by acdively managing risk
- Integrate real-time asset health data into decision-support and continuous comprovement of predictive models
- Reduce unuscheduled OTS event through tighter integration and rule-based automation

## 2. Stakeholders & Users

- Maintenance director
- Reliability engineering / Asset reliability team
- Maintenance planners and schedulers
- Floor supervisors / senior leadership
- Maintenance technicians (mobile)
- IT/OTT team
- Business intelligence analytics team
- Finance operations

## 3. Scope & Out-Of-Scope

Scope in-scope for this business use case:

-1. Deployment scope
  - Maximo Application Suite (MAS Manage) as the CM]S
  - IoT sensor layer with vibration/temperature sensors on critical assets
  - IoT platform/event ingestion, anomaly detection and rules
  - Integration layer between event platform and MATÅ Manage
  - Analytics/MS Ai for predictive models (outside of Maximo)

-2. Business scope
  - Avaidance predictive maintenance on critical assets
  - Auto-generated work order creation from io events for inspection/corrective maintenance
  - Feed loop of inspection results and failure data back to the predictive models
  - Integration of maintenance activity with F(ERP/FL]

-3. Expressed functional scope
  - Autom-classification of asset majority level in the event to prioritize work orders (e.g. Critical vers non-critical)
  - AXe rUmed-all ingration of Io data and work order data for BI/reporting

## 4. Current Challenges

- Upfront planned maintenance is not fitting real-time conditions of assets
- Separated silos of data in IO platforms and Maximo, each with duplicated structure and manual entry
- Difficulty of tight integration between IO platform and Maximo Manage
- Limited canability to cowharmonise rules and thresholds to automate work orders