# Zensus Data Loader

## Purpose

This folder contains teaching material and loader examples for official Zensus 2022 grid-cell data. The focus is on reproducible access to small-area census indicators, conversion from German grid IDs to geometries, and careful interpretation of aggregated demographic and housing variables.

Zensus grid data is useful as a spatial context layer for many course topics. Students can join it with Mapillary points, Airbnb listings, OSM features, or accident data to ask questions about population density, age structure, household size, rent, privacy-preserving aggregation, and the modifiable areal unit problem.

## Current Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/zensus/notebooks/zensus_mainz_cells_map.ipynb)

- `notebooks/zensus_mainz_cells_map.ipynb`

The notebook downloads Zensus 2022 grid-cell ZIP archives from the official Destatis page, selects the 100 m CSV tables, extracts cells around Mainz, joins selected demographic and housing variables, and visualizes the result on a Folium map.

## Data Source

- Destatis Zensus 2022 page: https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Zensus2022/_inhalt.html
- Files used: 100 m grid CSV tables from the official grid-cell ZIP archives
- The notebook writes temporary outputs to Colab's `/content/` directory by default.

## Planned Uses

- 100 m census-cell mapping
- Spatial joins with Mapillary, OSM, Airbnb, and accident data
- Discussion of aggregation, privacy protection, missing values, and spatial bias

## Notes

Raw and derived data should normally stay outside the repository. The notebook writes outputs to Colab's temporary `/content/` directory by default.
