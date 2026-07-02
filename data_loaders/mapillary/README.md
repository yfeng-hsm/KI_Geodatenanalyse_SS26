# Mapillary Data Loader

## Purpose

This folder contains teaching material for working with Mapillary street-level imagery metadata. The current notebook focuses on small, controlled API requests rather than large downloads. This keeps the example suitable for Colab, avoids excessive API load, and makes it easier to explain how image metadata is represented as geospatial point data.

Mapillary is useful in the course because it connects geospatial analysis with computer vision: image locations can be mapped, queried by bounding boxes or buffers, linked to trajectories, and later connected to CNN or multimodal workflows. The notebook deliberately starts with metadata and thumbnails before moving toward image modelling.

## Current Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/mapillary/notebooks/mapillary_api_loader_mainz.ipynb)

- `notebooks/mapillary_api_loader_mainz.ipynb`

The notebook is written in a Colab style. It explains how students can obtain a Mapillary API token, store it in Colab Secrets, query image metadata around the selected HS Mainz area, and visualize image points and thumbnails. It includes examples for bbox queries, a census-style 100 m cell, a point buffer, and a trajectory corridor.

Do not commit API tokens. Use Colab Secrets or a local environment variable named `MAPILLARY_ACCESS_TOKEN`.

## Data Source

- Mapillary Graph API: https://www.mapillary.com/developer/api-documentation/
- Access requires a Mapillary access token.
- The notebook requests only small metadata samples for teaching.

## Planned Uses

- Street-level image analysis
- CNN examples
- Vision Transformer examples
- Coverage and sampling bias discussion
- Linking image metadata to Zensus, OSM, and field survey data

## Loader Plan

- Document API or download workflow
- Define metadata fields and image storage conventions
- Add preprocessing steps for image size, labels, geolocation, and train-test splits
- Provide a Python loader function for image paths, metadata, and labels

## Proposed Structure

```text
mapillary/
├── README.md
├── src/
├── notebooks/
├── config/
└── tests/
```
