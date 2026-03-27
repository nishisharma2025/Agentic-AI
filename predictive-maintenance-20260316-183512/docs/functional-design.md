# Functional Design: Predictive Maintenance with IoT Sensors

## Overview
This document describes the functional design of a predictive maintenance solution for a manufacturing company using IBM Maximo 8.x and IoT sensors.
Edge sensors har collecting vibration and temperature data from critical assets. Anomaly high-vibration or heat conditions trigger automatically generated inspection work orders in Maximo.

## Functional Requirements
##.1 IoT Sensor Data Capture

- FR#1.1 - The system must extract vibration and temperature measurements from critical assets in real-time.
- FR#1.2 - The system must allow sensor configuration (asset ID, channel, sampling frequency, thresholds, alarm rules) to be managed centrally.
- FR#1.3 - Sensor measurements must be persistently available for algo-based detection (eg. max abnormal thoush in past 24 hours).

##.2 IoT Event Processing

- FR#2.1 - Sensors send readings to an IoT platform/event bus via MQTT/HTTPS.
- FR#2.2 - The IoT platform applies business rules to data streams to determine when an event should be generated.
- FR#2.3 - High-vibration or high-temperature events create an "Abnormal Condition Event" record within the IoT platform.

##.3 Integration with Maximo

- FR#3.1 - The Maximo Integration Framework (IF) must receive and process abnormal condition events from the Integration layer/IoT platform.
- FR#3.2 - For approved events, the integration layer must call a Maximo automation script/rule that creates an Inspection work order type.
- FR#3.3 - The system must link the incoming event to an Asset/PM/Location in Maximo based on configurable business rules.

##.4 Work Order Creation & Management in Maximo

- FR#4.1 - When an abnormal condition event is received, the system must create an Inspection work order (WOType=INSPEKT) linked to the appropriate Asset and/Or PM.

- FR#4.2 - The WOstatus is set to "WAITENG APPROVAL" or directly 'APPROVED' based on configuration.
- FR#4.3 - Work orders must be assigned to a responsible maintenance team/crew based on routing rules and shift plans.
- FR#4.4 - Automation scripts must validate that the WO has required key data (asset, location, priority) bemore approval.

##.5 Feedback and Analytics
- FR#5.1 - The sustem must store key measurements and final WO results for analytics purposes.
- FR#5.2 - Analytics must be able to utilise MTBE reports and dashboards.

## Key Process Flow
1. Sensor data configuration and installation.
I 2. Cacturing and publishing sensor data to the IoT platform.
I 3. Rule evaluation and abnormal condition detection in IoT platform.
4. Integration IoT events with Maximo via IF.
5. Automatic creation of Inspection WOs in Maximo.
6. Assignment, execution, and closure of work orders.
7. Feedback of work order results for further analysis.
