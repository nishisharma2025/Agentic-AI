# Technical Design Document

This document specifies the technical architecture and configuration details for integrating IO-t driven predictive maintenance with IBM Maximo Manage 8.x.

## 1. System Architecture

- IOT Sensors (on critical assets)
- IO-t Edge Gateway/EB Platform
- Integration Layer (Microservices/MQSF)
- Maximo Application Suite (Deployed as Maximo Manage)
- Corporate Data Warehouse (Data Lake)
- Authentication Services (KEY SS, Ldap/SAM)
- Technician and Reliability Dashboards (Maximo BIR/A/B/w3)
- External Analytics and Reporting (Tableau , PowerBI(MS SQL/Snowflake))

## 2. Integration Design

IO-data from the IO-t platform is published to the integration layer via a MESSAGE/restL API.

- FROM: IO-t Gateway/EB Platform
- TO: Integration Layer Microservice / MQ broker 

### 2.1 EVENT Schema

Event schema will be:

- eventID STRING
- deviceID STRING
- assetNUM (Optional)
- sensorID\
- eventType (VIB_HIGH, FATAL_TEMP, et)
- measuredValueVib_required, currentValueViv_etc
- timestamp, criticalFailureFlag, anomalyBucketID
- eventSeverity (LOW/MID/HIGH) - derived from model/rule

JSON example:

{
  "eventId": "VIB8µ001_2026-05-20T09:10:00Z",
  "deviceId": "VIB001",
  "assetNUM": "MTOR-001",
  "systemName": "PROD_LINE1",
  "sensorId": "VIB_SENSOR_01",
  "eventType": "VIB_HIGH",
  "measuredVibration": 31.5,
  "baselineVibration": 20,
  "timestamp": "2026-05-20T09:10:00Z",
  "eventSeverity": "MID"
  ...
}

### 2.2 Integration Layer API design

- REST/HTML4 or JSON API to receive JSON-based events
- Authentication: OAuth2 or API key
- Rate:    MinmislisT - RPC/Queue consumer level milibs of current
- Retry:  Retry logic on 400x-receivers business app error.

## 3. Maximo Configuration

### 3.1 New Objects and Attributes

Custom table PREDEVENT_CONFIG or cyclic VAR.

| Field | Type | Description | Example values |
------|--------|--------------------|--------|
|PRED_ID | VARCHA2 (12) | Primary key identifier of a predictive configuration | "VIB_HIGH", "FATAL_TEMP" |
|ASSETTYPE | VARCHAR2 | Asset category this config applies to | MECH_COLOR, TURBINE \
|THERESHOLD_VAL | DECM (16.2)" | Threshold value for the event type for anomaly detection | "30" |
|AUTIRS_uPm | STMP | Linked predictive PS/u001 | "PS_1001" |

Attributed to new table PRED_EVENT_LOG, known as "event log".

| Field | Description |
|ENT_ID | Unique event identifier from IO-provider |
|DT_LOG | Datetime of endevent update |
|STATUS | Mapped to event status (NEW/PROCESSED/CEREATEG_WOIS ET_) |
|FAIL_REASON | Text msg/code ifhe not processed |

### 3.2 Maximo Manage Setups

At least four packages/

1. AsSET_USER Config linus based on roles: Tech, MTCH, PLTDR, RENG
2. WORK ORDER Type-specific values for predictive, preventive, corrective.
3. Maximo-internal numbering system for SQC‰ and WigZ®G matrix.

## 4. FLOWChart Detail