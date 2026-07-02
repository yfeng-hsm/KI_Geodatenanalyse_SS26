# Airbnb Data Loader

## Purpose

This folder contains teaching material for working with open Airbnb listing data as geospatial point data. The examples use Inside Airbnb because it provides city-level CSV tables with listing attributes, latitude/longitude coordinates, and neighbourhood boundary files.

Airbnb data is useful for showing how ordinary tabular data becomes geodata: each listing row has coordinates, can be mapped as a point, can be joined to neighbourhood polygons, and can be aggregated into spatial indicators. It also gives students a concrete example of data quality questions around scraped platform data, missing values, price fields, room types, and neighbourhood-level interpretation.

## Current Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/airbnb/notebooks/airbnb_munich_points.ipynb)

- `notebooks/airbnb_munich_points.ipynb`

The notebook reads Inside Airbnb Munich listing points from the lightweight `visualisations/listings.csv` file, converts latitude/longitude columns to a GeoDataFrame, loads neighbourhood boundaries, maps listing points, demonstrates a spatial join, and writes a prepared GeoJSON output.

## Data Source

- Inside Airbnb data portal: https://insideairbnb.com/get-the-data/
- Example city: Munich, Bavaria, Germany
- Files used: `listings.csv` for point data and `neighbourhoods.geojson` for polygon boundaries
- License noted by Inside Airbnb: Creative Commons Attribution 4.0 International License

## Planned Uses

- Tabular machine learning examples
- Spatial feature engineering
- Neighborhood-level aggregation
- Model interpretation exercises
- Discussion of platform data, sampling bias, and uncertainty in scraped datasets

## Loader Plan

- Document source, license, and download procedure
- Define expected raw data files
- Add preprocessing steps for geometry, CRS, missing values, and target variables
- Provide a Python loader function returning clean tabular and geospatial data

## Proposed Structure

```text
airbnb/
├── README.md
├── src/
├── notebooks/
├── config/
└── tests/
```
