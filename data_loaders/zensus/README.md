# Zensus Data Loader

Zensus 2022 grid-cell data around Mainz.

## Notebook

- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/zensus/notebooks/zensus_mainz_cells_map.ipynb)
  [zensus_mainz_cells_map.ipynb](notebooks/zensus_mainz_cells_map.ipynb): downloads official 100 m grid-cell tables, extracts Mainz cells, joins selected indicators, and maps the result.

## Data

- Source: <https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Zensus2022/_inhalt.html>
- Files: official Zensus 2022 100 m grid-cell ZIP archives.
- Output: temporary Colab files and Folium map.
- Raw and derived Zensus files should normally stay outside the repository.
