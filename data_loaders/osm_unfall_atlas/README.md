# OSM Unfallatlas Data Loader

## Purpose

This folder is reserved for OpenStreetMap and Unfallatlas teaching material. The goal is to combine open road network data with official accident point data so students can practice spatial joins, network-based feature construction, and critical interpretation of safety datasets.

The planned loader should make it clear which data comes from volunteered geographic information and which data comes from official reporting. This distinction is important for discussions about completeness, reporting bias, exposure, road hierarchy, and what can or cannot be inferred from accident counts alone.

## Current Notebook

No notebook is available yet. When the OSM/Unfallatlas loader notebook is added, this README should include a direct Colab link here.

## Planned Data Sources

- OpenStreetMap data, for example via OSMnx, Geofabrik, or Overpass
- German Unfallatlas accident data from official statistical sources
- Optional administrative or grid boundaries for aggregation

## Planned Uses

- Spatial joins and overlays
- Road network and accessibility features
- Accident pattern analysis
- Graph-based deep learning examples
- Ethics and reporting bias discussion

## Loader Plan

- Document data sources, licenses, and download procedures
- Define expected OSM and Unfallatlas input files
- Add preprocessing steps for CRS handling, spatial joins, network extraction, and feature construction
- Provide Python loader functions for accident points, road network features, and joined analysis tables

## Proposed Structure

```text
osm_unfall_atlas/
├── README.md
├── src/
├── notebooks/
├── config/
└── tests/
```
