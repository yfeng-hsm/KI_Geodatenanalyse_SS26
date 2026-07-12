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

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/meinrad/notebooks/meinrad_mainz_live_dynamic_map.ipynb)

- `notebooks/meinrad_mainz_live_dynamic_map.ipynb`

The notebook reads snapshot CSV files already collected by GitHub Actions, maps the latest station availability with Folium, and creates a Leaflet time-slider map when several snapshots are available.

The notebook is intentionally read-only: it does not call the live API and does not create new snapshots. If no snapshot CSV exists yet, wait for GitHub Actions to collect data or reopen the latest repository version.

## Optional Raw Response

To save the full API response, including bike-level records:

```bash
python3 -m data_loaders.meinrad.src.meinrad_snapshot --save-raw
```

For long collection runs, prefer compressed raw output:

```bash
python3 -m data_loaders.meinrad.src.meinrad_snapshot --save-raw --compress-raw
```

Use this only when the teaching or research question requires vehicle-level information. For most course exercises, the station-level CSV is enough and avoids unnecessary collection of individual bike identifiers.

## Suggested Collection Schedule

For a first teaching dataset, run the script every 10 minutes for 2-4 weeks. This is enough to show morning/evening patterns, station imbalance, weekend effects, and weather joins.

Example cron-style schedule:

```text
*/10 * * * * cd /path/to/KI_Geodatenanalyse_SS26 && python3 -m data_loaders.meinrad.src.meinrad_snapshot
```

## GitHub Actions Collection

This repository includes `.github/workflows/collect-meinrad-2-weeks.yml` for a two-week collection run that does not depend on a local computer staying awake.

- Start: `2026-07-12 13:00 Europe/Berlin`
- End: `2026-07-26 12:00 Europe/Berlin`
- Trigger: external cron-job.org `workflow_dispatch`
- Interval: every 15 minutes at `:00`, `:15`, `:30`, and `:45` in `Europe/Berlin`
- Output folder: `data_loaders/meinrad/data/`
- Timestamp fields: both `collected_at_utc` and `collected_at_germany`
- Files per run: station CSV, summary JSON, and complete raw API response as `.json.gz`

The workflow commits collected CSV, summary JSON, and compressed raw JSON files back to the repository. GitHub's native `schedule` trigger is intentionally disabled to avoid duplicate runs when the external cron service triggers the same workflow. It can also be triggered manually from the GitHub Actions tab with `force_collect=true`.

One sampled run on 2026-07-12 produced approximately:

- station CSV: 45 KB
- summary JSON: 1 KB
- raw API JSON uncompressed: 748 KB
- raw API JSON compressed: 28-36 KB

At a 15-minute interval for 14 days, this is 1,344 snapshots. Expected repository working-tree size is roughly 100-110 MB when storing compressed raw JSON, or about 1.0 GB if raw JSON is kept uncompressed.

## Teaching Uses

- Real-time JSON API access
- Repeated snapshot collection
- Station availability maps
- Temporal aggregation by hour, weekday, and station
- Imbalance detection and simple demand proxies
- Joins with weather, OSM points of interest, slope, and public transport stops

## Limitations

The endpoint provides current availability snapshots, not official trip records. Origin-destination flows and rentals cannot be reconstructed reliably unless a long enough snapshot history is collected and interpreted carefully.
