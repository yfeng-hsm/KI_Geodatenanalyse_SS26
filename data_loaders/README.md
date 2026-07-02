# Data Loaders

This folder is reserved for reusable dataset access code and dataset documentation used across lectures and student projects.

The goal is to keep data loading, preprocessing, licensing notes, and reproducibility instructions separate from lecture-specific notebooks.

## Planned Datasets

| Folder | Dataset | Planned use |
| --- | --- | --- |
| `zensus/` | Zensus 2022 grid-cell data | 100 m census cells, demographic and housing variables, spatial joins |
| `airbnb/` | Airbnb data | Tabular and spatial ML examples |
| `mapillary/` | Mapillary data | Image-based deep learning examples |
| `osm_unfall_atlas/` | OSM and Unfallatlas data | Spatial analysis, graph features, accident analysis |

## Suggested Dataset Folder Structure

```text
dataset_name/
├── README.md
├── src/
├── notebooks/
├── config/
└── tests/
```

Raw data should not be committed unless licensing and file size make this appropriate. Prefer documented download or preparation steps.
