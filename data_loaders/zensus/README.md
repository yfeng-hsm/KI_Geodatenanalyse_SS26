# Zensus Data Loader

Zensus 2022 grid-cell data provides official German census indicators on a regular grid.

## Notebook

| Notebook | Data/Input | What it does | Output | Colab |
| --- | --- | --- | --- | --- |
| [zensus_mainz_cells_map.ipynb](notebooks/zensus_mainz_cells_map.ipynb) | Official Zensus 2022 100 m grid-cell ZIP archives | Downloads grid-cell tables, extracts cells around Mainz, joins selected demographic and housing variables, and visualizes the result. | Folium map and temporary Colab outputs | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/zensus/notebooks/zensus_mainz_cells_map.ipynb) |

## Data Source

| Item | Value |
| --- | --- |
| Source | <https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Zensus2022/_inhalt.html> |
| Files | 100 m grid CSV tables from official grid-cell ZIP archives |
| Local output | Colab `/content/` directory by default |

## Notes

| Item | Note |
| --- | --- |
| Repository data | Raw and derived Zensus files should normally stay outside the repository. |
| Joins | The grid can be joined with Mapillary points, Airbnb listings, OSM features, or accident data. |
