# Frankfurt Bike-Sharing Data Loader

Frankfurt subset from the TUM FTM European Bike-Sharing Dataset.

## Notebook

- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/frankfurt_bike_sharing/notebooks/frankfurt_bike_sharing_gcn_loader.ipynb)
  [frankfurt_bike_sharing_gcn_loader.ipynb](notebooks/frankfurt_bike_sharing_gcn_loader.ipynb): reads the filtered Frankfurt full-data zip, shows station availability time series, maps the station distribution, plots monthly trip activity, and maps the most frequently used bike's trip segments.

## Data

- Source repo: <https://github.com/TUMFTM/european-bike-sharing-dataset>
- Paper: `Data-Driven Insights into (E-)Bike-Sharing`, Transportation, 2025, DOI `10.1007/s11116-025-10661-2`.
- License: Creative Commons Attribution-NonCommercial 4.0 International (`CC BY-NC 4.0`).
- Frankfurt city id in the dataset: `8`.
- Full raw archive: source repository `full/dataset.zip`.
- Course notebook input: locally filtered `frankfurt_bike_sharing_full_filtered.zip`, stored outside Git and served through Seafile for Colab use.

## Local Filtered Outputs

The ignored `data/` folder may contain local or Seafile-uploaded artifacts such as:

- `frankfurt_full/stations_frankfurt.csv`
- `frankfurt_full/station_status_frankfurt.csv`
- `frankfurt_full/trips_frankfurt.csv`
- `frankfurt_bike_sharing_full_filtered.zip`

These files are intentionally not committed to GitHub.

## Graph Builder Script

The reusable Python module still supports building a compact GCN-ready station graph:

```bash
python3 -m data_loaders.frankfurt_bike_sharing.src.frankfurt_bike_sharing_gcn --download-sample
```

It downloads sample CSVs from the source repository, builds node and edge tables, and writes local outputs to `data_loaders/frankfurt_bike_sharing/data/`.

## Files

- `notebooks/`: Colab notebook.
- `src/`: reusable graph-builder code.
- `tests/`: small unit tests for graph construction.
- `data/`: ignored local outputs.
