# Mapillary Data Loader

Mapillary provides street-level imagery metadata through the Graph API. The current notebook requests small metadata samples instead of large image downloads.

## Notebook

| Notebook | Data/Input | What it does | Output | Colab |
| --- | --- | --- | --- | --- |
| [mapillary_api_loader_mainz.ipynb](notebooks/mapillary_api_loader_mainz.ipynb) | Mapillary access token and Mainz query areas | Queries image metadata, maps image points and thumbnails, and demonstrates bbox, grid-cell, buffer, and trajectory-corridor queries. | GeoDataFrames and maps in the notebook | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/mapillary/notebooks/mapillary_api_loader_mainz.ipynb) |

## Data Source

| Item | Value |
| --- | --- |
| API | <https://www.mapillary.com/developer/api-documentation/> |
| Access | Requires a Mapillary access token |
| Secret name | `MAPILLARY_ACCESS_TOKEN` |
| Download size | Small metadata samples only |

Do not commit API tokens. Use Colab Secrets or a local environment variable named `MAPILLARY_ACCESS_TOKEN`.

## Folders

| Folder | Contents |
| --- | --- |
| `notebooks/` | Mapillary API notebook |
| `config/` | Example environment configuration |
