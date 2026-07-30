# Frankfurt Bike-Sharing GCN Data Loader

Frankfurt subset from the TUM FTM European Bike-Sharing Dataset.

## Notebook

- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/frankfurt_bike_sharing/notebooks/frankfurt_bike_sharing_gcn_loader.ipynb)
  [frankfurt_bike_sharing_gcn_loader.ipynb](notebooks/frankfurt_bike_sharing_gcn_loader.ipynb): loads Frankfurt stations, builds GCN-ready node and edge tables, and maps the station graph.

## Data

- Source repo: <https://github.com/TUMFTM/european-bike-sharing-dataset>
- Paper: `Data-Driven Insights into (E-)Bike-Sharing`, Transportation, 2025, DOI `10.1007/s11116-025-10661-2`.
- License: Creative Commons Attribution-NonCommercial 4.0 International (`CC BY-NC 4.0`).
- Frankfurt city id in the dataset: `8`.
- Default notebook input: small `sample/*.csv` files from the source repo.

## GCN Output

- `nodes.csv`: one row per Frankfurt station.
- `edges.csv`: station-to-station graph edges.
- If Frankfurt trip rows are available, edges are aggregated from trips.
- If no Frankfurt trip rows are available in the sample, edges fall back to spatial k-nearest-neighbor station links.

## Script

- `python3 -m data_loaders.frankfurt_bike_sharing.src.frankfurt_bike_sharing_gcn --download-sample`
  downloads sample CSVs, builds the graph, and writes outputs to `data_loaders/frankfurt_bike_sharing/data/`.

## Files

- `notebooks/`: Colab notebook.
- `src/`: reusable loader code.
- `tests/`: small unit tests for graph construction.
- `data/`: ignored local outputs.
