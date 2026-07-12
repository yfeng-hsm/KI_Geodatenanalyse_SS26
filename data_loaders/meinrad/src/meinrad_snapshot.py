"""Collect station-level meinRad availability snapshots for Mainz.

The public nextbike endpoint also exposes bike-level identifiers. This loader
keeps the default output at station/place level for teaching use.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
import sys
import time as time_module
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_DOMAIN = "mz"
DEFAULT_CITY_UID = 755
DEFAULT_TIMEOUT_SECONDS = 30
DEFAULT_TIMESTAMP_TIMEZONE = "Europe/Berlin"
NEXTBIKE_URL = "https://api.nextbike.net/maps/nextbike-live.json"


class MeinRadSnapshotError(RuntimeError):
    """Raised when a meinRad snapshot cannot be fetched or parsed."""


def fetch_live_data(
    domain: str = DEFAULT_DOMAIN,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    """Fetch live data from the nextbike endpoint for a domain."""
    url = f"{NEXTBIKE_URL}?domains={domain}"
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "KI_Geodatenanalyse_SS26 meinRad teaching loader",
        },
    )

    try:
        with urlopen(request, timeout=timeout_seconds) as response:
            status = getattr(response, "status", None)
            if status and status >= 400:
                raise MeinRadSnapshotError(f"HTTP error {status} for {url}")
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise MeinRadSnapshotError(f"HTTP error {exc.code} for {url}") from exc
    except URLError as exc:
        raise MeinRadSnapshotError(f"Network error for {url}: {exc.reason}") from exc
    except json.JSONDecodeError as exc:
        raise MeinRadSnapshotError(f"Invalid JSON returned by {url}") from exc


def select_city(
    payload: dict[str, Any],
    city_uid: int = DEFAULT_CITY_UID,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return the country/system and city dictionaries for Mainz."""
    for country in payload.get("countries", []):
        for city in country.get("cities", []):
            if city.get("uid") == city_uid:
                return country, city
    raise MeinRadSnapshotError(
        f"City uid {city_uid} not found. Use domains=mz rather than city=755."
    )


def convert_utc_to_timezone(utc_dt: datetime, timezone_name: str) -> datetime:
    """Convert a UTC datetime to a named timezone without requiring extra packages."""
    if timezone_name in {"UTC", "Etc/UTC", "Z"}:
        return utc_dt.astimezone(timezone.utc)

    try:
        from zoneinfo import ZoneInfo

        return utc_dt.astimezone(ZoneInfo(timezone_name))
    except Exception:
        if not hasattr(time_module, "tzset"):
            raise MeinRadSnapshotError(
                f"Timezone {timezone_name!r} requires Python zoneinfo support."
            )

        old_tz = os.environ.get("TZ")
        try:
            os.environ["TZ"] = timezone_name
            time_module.tzset()
            return utc_dt.astimezone()
        finally:
            if old_tz is None:
                os.environ.pop("TZ", None)
            else:
                os.environ["TZ"] = old_tz
            time_module.tzset()


def build_summary(
    country: dict[str, Any],
    city: dict[str, Any],
    collected_at_utc: str,
    collected_at_germany: str | None = None,
) -> dict[str, Any]:
    """Create a compact metadata summary for one snapshot."""
    places = city.get("places", [])
    stations = [place for place in places if place.get("spot")]
    floating_bikes = [place for place in places if place.get("bike")]
    return {
        "collected_at_utc": collected_at_utc,
        "collected_at_germany": collected_at_germany,
        "system_name": country.get("name"),
        "domain": country.get("domain"),
        "city_uid": city.get("uid"),
        "city_name": city.get("name"),
        "num_places": city.get("num_places"),
        "places_returned": len(places),
        "station_places": len(stations),
        "floating_bike_places": len(floating_bikes),
        "set_point_bikes": city.get("set_point_bikes"),
        "available_bikes": city.get("available_bikes"),
        "return_to_official_only": city.get("return_to_official_only"),
        "refresh_rate": city.get("refresh_rate"),
        "bike_types": city.get("bike_types", {}),
        "source_url": f"{NEXTBIKE_URL}?domains={country.get('domain', DEFAULT_DOMAIN)}",
    }


def flatten_places(
    country: dict[str, Any],
    city: dict[str, Any],
    collected_at_utc: str,
    collected_at_germany: str | None = None,
) -> list[dict[str, Any]]:
    """Flatten nextbike places to one row per station/place."""
    rows: list[dict[str, Any]] = []
    for place in city.get("places", []):
        rows.append(
            {
                "collected_at_utc": collected_at_utc,
                "collected_at_germany": collected_at_germany,
                "system_name": country.get("name"),
                "domain": country.get("domain"),
                "city_uid": city.get("uid"),
                "city_name": city.get("name"),
                "place_uid": place.get("uid"),
                "place_number": place.get("number"),
                "name": place.get("name"),
                "address": place.get("address"),
                "lat": place.get("lat"),
                "lng": place.get("lng"),
                "is_station": bool(place.get("spot")),
                "is_floating_bike": bool(place.get("bike")),
                "active_place": place.get("active_place"),
                "maintenance": bool(place.get("maintenance")),
                "terminal_type": place.get("terminal_type"),
                "place_type": place.get("place_type"),
                "booked_bikes": place.get("booked_bikes"),
                "bikes": place.get("bikes"),
                "bikes_available_to_rent": place.get("bikes_available_to_rent"),
                "bike_racks": place.get("bike_racks"),
                "free_racks": place.get("free_racks"),
                "special_racks": place.get("special_racks"),
                "free_special_racks": place.get("free_special_racks"),
                "bike_types_json": json.dumps(
                    place.get("bike_types", {}), ensure_ascii=False, sort_keys=True
                ),
                "bike_count_from_list": len(place.get("bike_list", [])),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    """Write rows to CSV with stable field order."""
    if not rows:
        raise MeinRadSnapshotError("No place rows to write.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, data: dict[str, Any]) -> None:
    """Write indented UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_json_gzip(path: Path, data: dict[str, Any]) -> None:
    """Write compressed UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write("\n")


def collect_snapshot(
    output_dir: Path,
    domain: str = DEFAULT_DOMAIN,
    city_uid: int = DEFAULT_CITY_UID,
    save_raw: bool = False,
    compress_raw: bool = False,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
    timestamp_timezone: str = DEFAULT_TIMESTAMP_TIMEZONE,
) -> dict[str, Any]:
    """Fetch, validate, flatten, and write one meinRad snapshot."""
    collected_at = datetime.now(timezone.utc)
    collected_at_utc = collected_at.isoformat(timespec="seconds")
    collected_at_local = convert_utc_to_timezone(collected_at, timestamp_timezone)
    collected_at_germany = collected_at_local.isoformat(timespec="seconds")
    stamp = collected_at_local.strftime("%Y%m%dT%H%M%S")

    payload = fetch_live_data(domain=domain, timeout_seconds=timeout_seconds)
    country, city = select_city(payload, city_uid=city_uid)
    summary = build_summary(country, city, collected_at_utc, collected_at_germany)
    rows = flatten_places(country, city, collected_at_utc, collected_at_germany)

    csv_path = output_dir / f"meinrad_mainz_places_berlin_{stamp}.csv"
    summary_path = output_dir / f"meinrad_mainz_summary_berlin_{stamp}.json"
    write_csv(csv_path, rows)
    write_json(summary_path, summary)

    raw_path = None
    if save_raw:
        if compress_raw:
            raw_path = output_dir / f"meinrad_mainz_raw_berlin_{stamp}.json.gz"
            write_json_gzip(raw_path, payload)
        else:
            raw_path = output_dir / f"meinrad_mainz_raw_berlin_{stamp}.json"
            write_json(raw_path, payload)

    return {
        "summary": summary,
        "places_csv": str(csv_path),
        "summary_json": str(summary_path),
        "raw_json": str(raw_path) if raw_path else None,
    }


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Collect one station-level meinRad availability snapshot for Mainz."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data",
        help="Directory for CSV/JSON snapshot outputs.",
    )
    parser.add_argument("--domain", default=DEFAULT_DOMAIN, help="nextbike domain, default: mz")
    parser.add_argument(
        "--city-uid",
        type=int,
        default=DEFAULT_CITY_UID,
        help="Mainz city uid in the nextbike feed, default: 755",
    )
    parser.add_argument(
        "--save-raw",
        action="store_true",
        help="Also save the complete API response, including bike-level records.",
    )
    parser.add_argument(
        "--compress-raw",
        action="store_true",
        help="Save the complete raw API response as .json.gz. Requires --save-raw.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help="Network timeout in seconds.",
    )
    parser.add_argument(
        "--timestamp-timezone",
        default=DEFAULT_TIMESTAMP_TIMEZONE,
        help="Timezone used for local timestamp columns and filenames.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])
    try:
        result = collect_snapshot(
            output_dir=args.output_dir,
            domain=args.domain,
            city_uid=args.city_uid,
            save_raw=args.save_raw,
            compress_raw=args.compress_raw,
            timeout_seconds=args.timeout,
            timestamp_timezone=args.timestamp_timezone,
        )
    except MeinRadSnapshotError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    summary = result["summary"]
    print(
        "Collected meinRad Mainz snapshot: "
        f"{summary['places_returned']} places, "
        f"{summary['available_bikes']} available bikes."
    )
    print(f"Places CSV: {result['places_csv']}")
    print(f"Summary JSON: {result['summary_json']}")
    if result["raw_json"]:
        print(f"Raw JSON: {result['raw_json']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
