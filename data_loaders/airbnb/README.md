# Airbnb Data Loader

Inside Airbnb Munich listing data as geospatial points.

## Notebook

- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/airbnb/notebooks/airbnb_munich_points.ipynb)
  [airbnb_munich_points.ipynb](notebooks/airbnb_munich_points.ipynb): loads Munich listings, converts coordinates to points, joins neighbourhoods, maps listings, and writes prepared GeoJSON.

## Data

- Source: <https://insideairbnb.com/get-the-data/>
- Example city: Munich, Bavaria, Germany.
- Files: `visualisations/listings.csv`, optional `data/listings.csv.gz`, `neighbourhoods.geojson`.
- Source license note: Creative Commons Attribution 4.0 International License.

## Files

- `notebooks/`: Airbnb loading and mapping notebook.
- `src/`, `config/`, `tests/`: reserved for reusable loader code and tests.
