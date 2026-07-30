# Airbnb Data Loader

Inside Airbnb provides city-level CSV tables with listing attributes, latitude/longitude coordinates, and neighbourhood boundary files.

## Notebook

| Notebook | Data/Input | What it does | Output | Colab |
| --- | --- | --- | --- | --- |
| [airbnb_munich_points.ipynb](notebooks/airbnb_munich_points.ipynb) | Munich `listings.csv`, optional `listings.csv.gz`, `neighbourhoods.geojson` | Converts listings to point geometries, joins neighbourhood polygons, maps listings, and prepares selected attributes. | Prepared GeoJSON | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/airbnb/notebooks/airbnb_munich_points.ipynb) |

## Data Source

| Item | Value |
| --- | --- |
| Portal | <https://insideairbnb.com/get-the-data/> |
| Example city | Munich, Bavaria, Germany |
| Files | `visualisations/listings.csv`, `data/listings.csv.gz`, `neighbourhoods.geojson` |
| License noted by source | Creative Commons Attribution 4.0 International License |

## Folders

| Folder | Contents |
| --- | --- |
| `notebooks/` | Airbnb loading and mapping notebook |
| `src/` | Reserved for reusable loader code |
| `config/` | Reserved for configuration |
| `tests/` | Reserved for tests |
