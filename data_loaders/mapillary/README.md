# Mapillary Data Loader

## Purpose

This folder will contain documentation and reusable loading code for Mapillary data used in image-based and multimodal geospatial AI examples.

## Planned Uses

- Street-level image analysis
- CNN examples
- Vision Transformer examples
- Coverage and sampling bias discussion

## Current Notebook

- `notebooks/mapillary_api_loader_mainz.ipynb`

The notebook is written in a Colab style. It explains how students can obtain a Mapillary API token, store it in Colab Secrets, query image metadata around Mainz, and visualize image points and thumbnails. It includes examples for bbox queries, a census-style 100 m cell, a point buffer, and a trajectory corridor.

Do not commit API tokens. Use Colab Secrets or a local environment variable named `MAPILLARY_ACCESS_TOKEN`.

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
