# meinRad Mainz Data Loader

Live availability snapshots from the Mainz `meinRad` bike-sharing system.

## Notebook

- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/meinrad/notebooks/meinrad_mainz_live_dynamic_map.ipynb)
  [meinrad_mainz_live_dynamic_map.ipynb](notebooks/meinrad_mainz_live_dynamic_map.ipynb): loads committed snapshot CSVs, maps latest station availability, and creates a time-slider map.

The notebook is read-only. It does not call the live API. If CSVs are missing locally, it downloads the GitHub repository archive once and extracts the committed CSV files.

## Data

- Endpoint: `https://api.nextbike.net/maps/nextbike-live.json?domains=mz`
- System: `meinRad`
- City: Mainz
- City UID: `755`
- Use `?domains=mz`; querying `?city=755` alone currently returns an empty response.

## Current Repository Data

- CSV snapshots: `1240`
- Summary JSON files: `1240`
- Raw compressed JSON files: `1240`
- Total station/place rows across CSV snapshots: `252721`
- First CSV checked locally: `meinrad_mainz_places_berlin_20260712T130051.csv`
- Latest CSV checked locally: `meinrad_mainz_places_berlin_20260725T121525.csv`
- Latest CSV rows: `213`
- Latest station rows: `192`
- Latest floating-bike rows: `21`
- Latest available bikes from CSV sum: `1158`

The row counts can look smaller than expected:

- The CSV is station/place-level, not bike-level.
- One CSV row is one station or floating-bike place.
- Bike counts are in `bikes_available_to_rent` and `bike_count_from_list`.
- Raw `.json.gz` files keep the complete API response, including bike-level lists.
- The workflow ran every 15 minutes. From `2026-07-12 13:00` to `2026-07-25 12:15`, that is about `1245` slots; `1240` committed CSV snapshots is close to that.
- A full two-week run every 10 minutes would be about `2016` snapshots.

## Snapshot Script

- `python3 -m data_loaders.meinrad.src.meinrad_snapshot`
  writes one station/place CSV and one summary JSON to `data_loaders/meinrad/data/`.
- `python3 -m data_loaders.meinrad.src.meinrad_snapshot --save-raw`
  also writes the complete raw API JSON response.
- `python3 -m data_loaders.meinrad.src.meinrad_snapshot --save-raw --compress-raw`
  writes the raw API response as compressed `.json.gz`.

## Output Files

- `meinrad_mainz_places_<timestamp>.csv`: station/place rows with coordinates, available bikes, racks, maintenance state, and bike-type counts.
- `meinrad_mainz_summary_<timestamp>.json`: snapshot metadata and city-level counts.
- `meinrad_mainz_raw_<timestamp>.json.gz`: complete compressed API response.

## GitHub Actions Collection

- Workflow: `.github/workflows/collect-meinrad-2-weeks.yml`
- Run window: `2026-08-01 12:25` to `2026-08-08 12:25 Europe/Berlin`
- Trigger: external cron-job.org `workflow_dispatch`
- Interval: every 15 minutes
- Output folder: `data_loaders/meinrad/data/`

External cron calls:

```text
POST https://api.github.com/repos/yfeng-hsm/KI_Geodatenanalyse_SS26/actions/workflows/collect-meinrad-2-weeks.yml/dispatches
```

Request body:

```json
{"ref":"main","inputs":{"force_collect":"false"}}
```

## Limitations

- The endpoint provides availability snapshots, not official trip records.
- Origin-destination flows cannot be reconstructed reliably from these snapshots alone.
- Raw responses can include bike identifiers; the station/place CSV omits individual bike IDs.
