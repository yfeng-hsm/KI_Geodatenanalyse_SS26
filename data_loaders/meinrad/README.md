# meinRad Mainz Data Loader

This folder collects and visualizes live availability snapshots from the Mainz `meinRad` bike-sharing system. The source is the public nextbike live endpoint for the `mz` domain.

## Notebook

| Notebook | Data/Input | What it does | Output | Colab |
| --- | --- | --- | --- | --- |
| [meinrad_mainz_live_dynamic_map.ipynb](notebooks/meinrad_mainz_live_dynamic_map.ipynb) | Snapshot CSV files in `data_loaders/meinrad/data/` | Loads committed snapshot CSVs, maps the latest station availability with Folium, and creates a Leaflet time-slider map when multiple snapshots exist. If CSVs are missing locally, it downloads the GitHub repository archive once and extracts the committed CSV files. | Interactive maps and summary tables | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/data_loaders/meinrad/notebooks/meinrad_mainz_live_dynamic_map.ipynb) |

The notebook is read-only: it does not call the live meinRad API and does not create new snapshots.

## Data Source

| Item | Value |
| --- | --- |
| Live endpoint | `https://api.nextbike.net/maps/nextbike-live.json?domains=mz` |
| System | `meinRad` |
| City | Mainz |
| City UID | `755` |
| Tested | `2026-07-12`: HTTP 200 for `domains=mz`, 222 places, more than 1,100 available bikes |

Querying `?city=755` alone currently returns an empty response. Use `?domains=mz` and then select city UID `755` from the returned payload.

## Snapshot Script

| Command | Output |
| --- | --- |
| `python3 -m data_loaders.meinrad.src.meinrad_snapshot` | Writes one station/place CSV and one summary JSON to `data_loaders/meinrad/data/`. |
| `python3 -m data_loaders.meinrad.src.meinrad_snapshot --save-raw` | Also writes the complete raw API JSON response, including bike-level records. |
| `python3 -m data_loaders.meinrad.src.meinrad_snapshot --save-raw --compress-raw` | Writes the raw API response as compressed `.json.gz`. |

## Output Files

| File pattern | Contents | Git |
| --- | --- | --- |
| `meinrad_mainz_places_<timestamp>.csv` | One row per station/place, with coordinates, available bikes, racks, maintenance state, bike-type counts, and no individual bike IDs. | Ignored locally unless intentionally committed by collection workflow |
| `meinrad_mainz_summary_<timestamp>.json` | Snapshot metadata and city-level counts. | Ignored locally unless intentionally committed by collection workflow |
| `meinrad_mainz_raw_<timestamp>.json.gz` | Complete compressed API response, including bike-level records. | Large over time; use only when needed |

## GitHub Actions Collection

| Item | Value |
| --- | --- |
| Workflow | `.github/workflows/collect-meinrad-2-weeks.yml` |
| Start | `2026-07-12 13:00 Europe/Berlin` |
| End | `2026-07-26 12:00 Europe/Berlin` |
| Trigger | external cron-job.org `workflow_dispatch` |
| Interval | every 15 minutes at `:00`, `:15`, `:30`, and `:45` in `Europe/Berlin` |
| Output folder | `data_loaders/meinrad/data/` |
| Timestamp fields | `collected_at_utc`, `collected_at_germany` |
| Files per run | station CSV, summary JSON, compressed raw API response |

External cron calls the GitHub workflow dispatch endpoint:

```text
POST https://api.github.com/repos/yfeng-hsm/KI_Geodatenanalyse_SS26/actions/workflows/collect-meinrad-2-weeks.yml/dispatches
```

Required headers:

```text
Authorization: Bearer <YOUR_GITHUB_TOKEN>
Accept: application/vnd.github+json
Content-Type: application/json
```

Request body:

```json
{"ref":"main","inputs":{"force_collect":"false"}}
```

One sampled run on `2026-07-12` produced approximately:

| File | Size |
| --- | --- |
| station CSV | 45 KB |
| summary JSON | 1 KB |
| raw API JSON uncompressed | 748 KB |
| raw API JSON compressed | 28-36 KB |

At a 15-minute interval for 14 days, this is 1,344 snapshots. Expected repository working-tree size is roughly 100-110 MB when storing compressed raw JSON, or about 1.0 GB if raw JSON is kept uncompressed.

## Limitations

| Item | Limitation |
| --- | --- |
| Availability snapshots | The endpoint provides current availability, not official trip records. |
| Origin-destination flows | Rentals cannot be reconstructed reliably from snapshots alone. |
| Bike-level records | Raw responses can include bike identifiers; the station CSV omits them. |
