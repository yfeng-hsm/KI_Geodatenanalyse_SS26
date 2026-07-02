# Zensus Data Loader

## Purpose

This folder contains teaching material and loader examples for official Zensus 2022 grid-cell data.

## Current Notebook

- `notebooks/zensus_mainz_cells_map.ipynb`

The notebook downloads Zensus 2022 grid-cell ZIP archives from the official Destatis page, selects the 100 m CSV tables, extracts cells around Mainz, joins selected demographic and housing variables, and visualizes the result on a Folium map.

## Planned Uses

- 100 m census-cell mapping
- Spatial joins with Mapillary, OSM, Airbnb, and accident data
- Discussion of aggregation, privacy protection, missing values, and spatial bias

## Notes

Raw and derived data should normally stay outside the repository. The notebook writes outputs to Colab's temporary `/content/` directory by default.
