# Mapillary Data Loader

Mapillary street-level imagery metadata around Mainz.

## Notebook

- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/mapillary/notebooks/mapillary_api_loader_mainz.ipynb)
  [mapillary_api_loader_mainz.ipynb](notebooks/mapillary_api_loader_mainz.ipynb): queries small metadata samples, maps image points and thumbnails, and demonstrates bbox, grid-cell, buffer, and trajectory-corridor queries.

## Data

- API: <https://www.mapillary.com/developer/api-documentation/>
- Requires a Mapillary access token.
- Secret name: `MAPILLARY_ACCESS_TOKEN`.
- Do not commit API tokens.

## Files

- `notebooks/`: Mapillary API notebook.
- `config/`: example environment configuration.
