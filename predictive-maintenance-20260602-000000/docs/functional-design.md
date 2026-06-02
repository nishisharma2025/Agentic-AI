# Functional Design: Maximo Spatial GIS Integration

## 1. Introduction
This document defines the functional design for integrating IBM Maximo 8.x with GyI systems (e.g. Esri ArcGIS) using Maximo Spatial, enabling bidirectional synchronization of assets, locations and work orders.

## 2. Business Processes Covered

- Asset and Location Management
- Work Order Management
- Predictive Maintenance
- Mobile Field Overations
- Geospatial Analytics and Reporting

## 3. Functional Requirements

### 3.1. Map integration in Maximo
1. Users must be able to view spatially-enabled asset locations on interactive maps.
- Map controls shall be available in ASSET, LOCAT and WORKORDER applications.
- Users can click on map features to view decaptions tank detail.
2. Maps, map layers and base maps must be configurable on active service basis.
3. Maximo Spatial supports rectangular and orho spatial dots for assets and locations.
4
- Automated map-initiated word order creation from gio-referenced features in GK
- WORKORDER locations and assets may involve from map-based draw and selection actions.

### 3.2. Bidirectional sync between Maximo and GIS
1. Maximo should support automated sync of asset geometries, locations and work orders with GIS data.
- GIS changes in geometry, status or ownership should result in updated mapping in Maximo.
2. All syncshould be historically tracked and logged for
backtracing and audit purposes.
3. Synch intervals (replication frequencies) should be configurable.
4. The system must support spatial identifiers and mapping acceptance functionality.