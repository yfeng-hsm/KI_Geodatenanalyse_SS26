# meinRad Mainz Data Loader

## Purpose

This folder contains a small loader for collecting live availability snapshots from the Mainz `meinRad` bike-sharing system. The source is the public nextbike live endpoint for the `mz` domain.

The loader is intended for teaching time-dependent geospatial data collection. It stores one row per station/place and can be run repeatedly, for example every 5-15 minutes, to build a local history of bike availability.

## Data Source

- Live endpoint: `https://api.nextbike.net/maps/nextbike-live.json?domains=mz`
- System: `meinRad`
- City: Mainz
- City UID in the feed: `755`

Important: querying `?city=755` alone currently returns an empty response. Use `?domains=mz` and then select city UID `755` from the returned payload.

## Current Test

The live endpoint was tested on 2026-07-12. It returned HTTP 200 for `domains=mz` and included Mainz data with 222 places and more than 1,100 currently available bikes. This means station-level snapshot collection can start.

## Run One Snapshot

From the repository root:

```bash
python3 -m data_loaders.meinrad.src.meinrad_snapshot
```

By default, outputs are written to `data_loaders/meinrad/data/`, which is ignored by Git:

- `meinrad_mainz_places_<timestamp>.csv`
- `meinrad_mainz_summary_<timestamp>.json`

The CSV keeps station/place-level attributes such as coordinates, available bikes, racks, maintenance state, and bike-type counts. It does not include individual bike IDs.

## Notebook

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/meinrad/notebooks/meinrad_mainz_dynamic_map.ipynb)

- `notebooks/meinrad_mainz_dynamic_map.ipynb`

The notebook reads all collected snapshot CSV files, maps the latest station availability, and creates an animated map when several snapshots are available.

## Optional Raw Response

To save the full API response, including bike-level records:

```bash
python3 -m data_loaders.meinrad.src.meinrad_snapshot --save-raw
```

Use this only when the teaching or research question requires vehicle-level information. For most course exercises, the station-level CSV is enough and avoids unnecessary collection of individual bike identifiers.

## Suggested Collection Schedule

For a first teaching dataset, run the script every 10 minutes for 2-4 weeks. This is enough to show morning/evening patterns, station imbalance, weekend effects, and weather joins.

Example cron-style schedule:

```text
*/10 * * * * cd /path/to/KI_Geodatenanalyse_SS26 && python3 -m data_loaders.meinrad.src.meinrad_snapshot
```

## Teaching Uses

- Real-time JSON API access
- Repeated snapshot collection
- Station availability maps
- Temporal aggregation by hour, weekday, and station
- Imbalance detection and simple demand proxies
- Joins with weather, OSM points of interest, slope, and public transport stops

## Limitations

The endpoint provides current availability snapshots, not official trip records. Origin-destination flows and rentals cannot be reconstructed reliably unless a long enough snapshot history is collected and interpreted carefully.
