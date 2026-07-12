# Data Loaders

This folder contains reusable dataset access notebooks and documentation for the course. The loaders are intentionally kept separate from lecture notebooks so that students can first understand where data comes from, how it is licensed, how it is converted into spatial formats, and how it can be reused in later analysis or modelling tasks.

Each dataset folder follows the same basic idea:

- a short README with purpose, data source, and teaching use cases,
- a Colab-ready notebook when a runnable loader already exists,
- optional `src/`, `config/`, and `tests/` folders for reusable code and configuration,
- no committed raw data unless licensing and file size make that appropriate.

## Current Loaders

| Folder | Dataset | Notebook | Teaching use |
| --- | --- | --- | --- |
| `zensus/` | Zensus 2022 grid-cell data | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/zensus/notebooks/zensus_mainz_cells_map.ipynb) | 100 m census cells, demographic and housing variables, spatial joins |
| `airbnb/` | Inside Airbnb data | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/airbnb/notebooks/airbnb_munich_points.ipynb) | Listing points, tabular features, neighbourhood aggregation |
| `mapillary/` | Mapillary street-level imagery metadata | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/mapillary/notebooks/mapillary_api_loader_mainz.ipynb) | API access, image metadata, point/buffer/trajectory queries |
| `osm_unfall_atlas/` | OSM and Unfallatlas data | Planned | Spatial analysis, graph features, accident analysis |
| `meinrad/` | meinRad Mainz bike-sharing snapshots | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/meinrad/notebooks/meinrad_mainz_dynamic_map.ipynb) | Live API snapshots, station availability, temporal demand proxies |

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
