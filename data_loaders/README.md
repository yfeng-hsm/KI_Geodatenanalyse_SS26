# Data Loaders

Reusable data access notebooks and dataset notes.

| Folder | Data | Notebook | What it does | Colab |
| --- | --- | --- | --- | --- |
| [`zensus/`](zensus/) | Zensus 2022 100 m grid-cell data | [zensus_mainz_cells_map.ipynb](zensus/notebooks/zensus_mainz_cells_map.ipynb) | Downloads official grid-cell tables, extracts Mainz cells, joins indicators, and maps the result. | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/zensus/notebooks/zensus_mainz_cells_map.ipynb) |
| [`airbnb/`](airbnb/) | Inside Airbnb Munich listings and neighbourhood boundaries | [airbnb_munich_points.ipynb](airbnb/notebooks/airbnb_munich_points.ipynb) | Loads listing points, joins neighbourhood polygons, maps listings, and writes prepared GeoJSON. | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/airbnb/notebooks/airbnb_munich_points.ipynb) |
| [`mapillary/`](mapillary/) | Mapillary street-level imagery metadata | [mapillary_api_loader_mainz.ipynb](mapillary/notebooks/mapillary_api_loader_mainz.ipynb) | Queries small metadata samples around Mainz areas and maps images, buffers, and trajectories. | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/mapillary/notebooks/mapillary_api_loader_mainz.ipynb) |
| [`osm_unfall_atlas/`](osm_unfall_atlas/) | OpenStreetMap and German Unfallatlas accident data | Planned | Reserved for OSM road-network and accident-point loading. | Planned |
| [`meinrad/`](meinrad/) | meinRad Mainz bike-sharing snapshots | [meinrad_mainz_live_dynamic_map.ipynb](meinrad/notebooks/meinrad_mainz_live_dynamic_map.ipynb) | Loads committed snapshot CSVs, maps latest station availability, and creates a time-slider map. | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/meinrad/notebooks/meinrad_mainz_live_dynamic_map.ipynb) |

| Common folder | Contents |
| --- | --- |
| `README.md` | Dataset source, notebook table, and notes |
| `notebooks/` | Colab-ready notebooks |
| `src/` | Reusable Python loader code when available |
| `config/` | Example configuration files when needed |
| `tests/` | Tests for reusable loader code when available |

Raw data should stay outside the repository unless the license and file size are suitable for committing.
