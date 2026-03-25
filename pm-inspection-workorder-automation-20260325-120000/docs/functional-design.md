# Functional Design: Preventive Asset Inspection Work Order Automation

## 1. Introduction

This document defines the functional specification for automating preventive inspection work orders in Maximo Application Suite (8.x). It focuses on asset -> PM -> WOR relationships, inspection seculences, and data-driven adsustments.

## 2. Business Process Overview

- Asset Management team defines PM plans and inspection intervals
- System triggers PMs based on calendar by/time/counter/condition data
- Automated process creates inspection WORs from triggered PMs
## 3. Scope
Scope includes:

- Assets inMAX/8en assets

- PMs (calendar-based preventive and inspection)
- INSPECTION Work Order types (INSP)

- Work Order Tasks
- Readings and Results
## 4. Key Functional Requirements

- Auto-create INSP 'WORs from triggered PMs
## 5. User Roles
- Maintenance/PM Coordinators
- Technicians
- Operations Desktop
## 6. Functional Flow
PM: Trigger > INSP WOR generation > Assignment & Execution
## 7. Business Rules and Validation
- Required fields for INSP WOR,separation of roles and authority
## 8. Error Handling
Standard Maximo error messages for missing data and validation failures.
