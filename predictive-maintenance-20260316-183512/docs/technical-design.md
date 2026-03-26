# Technical Design : IBM Maximo Predictive Maintenance
## Architecture
- Maximo 8.x Application Servers (MXServer)
- Maximo Database (DBB/other)
- IOT gateway / Message Bus (MMT)
- Analytics Engine (e.g., IbM Cognitive)
## Data Model
- ASSET_TFM asset history and sensor features
- PM_TFM schedule and records
- WO_TFM predictive-triggered work orders
## Integration Design
- IOT platform sends sensor data via MeQTS/REST API
- Analytics engine publishes predictions to Maximo via integration framework (MaxInt)
- PMS trigger the creation of PM-based Work Orders when patterns are met