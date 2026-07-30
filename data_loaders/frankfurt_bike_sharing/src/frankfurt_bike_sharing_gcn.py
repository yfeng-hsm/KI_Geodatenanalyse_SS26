"""Build a GCN-ready Frankfurt bike-sharing station graph.

The loader uses the TUM FTM European Bike-Sharing Dataset. It can work with
the small sample CSV files from GitHub or with locally downloaded full CSVs.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import shutil
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SOURCE_REPO = "https://github.com/TUMFTM/european-bike-sharing-dataset"
RAW_SAMPLE_BASE_URL = (
    "https://raw.githubusercontent.com/TUMFTM/european-bike-sharing-dataset/main/sample"
)
CITY_NAME = "Frankfurt"
CITY_COUNTRY = "DE"
DEFAULT_K_NEIGHBORS = 4
SAMPLE_FILES = ("cities.csv", "stations.csv", "trips.csv", "station_status.csv")


class FrankfurtBikeSharingError(RuntimeError):
    """Raised when the Frankfurt bike-sharing graph cannot be built."""


def download_sample_files(output_dir: Path, timeout_seconds: int = 60) -> list[Path]:
    """Download the small source-repo sample CSV files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    downloaded = []
    for filename in SAMPLE_FILES:
        url = f"{RAW_SAMPLE_BASE_URL}/{filename}"
        target = output_dir / filename
        request = Request(
            url,
            headers={"User-Agent": "KI_Geodatenanalyse_SS26 Frankfurt bike loader"},
        )
        try:
            with urlopen(request, timeout=timeout_seconds) as response:
                target.write_bytes(response.read())
        except HTTPError as exc:
            raise FrankfurtBikeSharingError(f"HTTP error {exc.code} for {url}") from exc
        except URLError as exc:
            if not shutil.which("curl"):
                raise FrankfurtBikeSharingError(
                    f"Network error for {url}: {exc.reason}"
                ) from exc
            try:
                subprocess.run(
                    ["curl", "-L", "--fail", "--silent", "--show-error", "-o", str(target), url],
                    check=True,
                    timeout=timeout_seconds,
                )
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as curl_exc:
                raise FrankfurtBikeSharingError(
                    f"Network error for {url}: {exc.reason}"
                ) from curl_exc
        downloaded.append(target)
    return downloaded


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    """Read a CSV file into dictionaries."""
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def parse_float(value: Any, default: float = 0.0) -> float:
    """Parse numeric CSV values while tolerating blanks."""
    if value in {None, ""}:
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def select_city_id(
    cities: list[dict[str, str]],
    city_name: str = CITY_NAME,
    country: str = CITY_COUNTRY,
) -> str:
    """Find the exact Frankfurt city id, avoiding Frankenthal matches."""
    for row in cities:
        if row.get("name") == city_name and row.get("country") == country:
            return row["id"]
    raise FrankfurtBikeSharingError(f"City {city_name!r} in country {country!r} not found.")


def summarize_station_status(
    station_status: list[dict[str, str]],
    station_ids: set[str],
) -> dict[str, dict[str, float]]:
    """Compute compact status features per station."""
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in station_status:
        station_id = row.get("station_id", "")
        if station_id in station_ids:
            grouped[station_id].append(row)

    summaries: dict[str, dict[str, float]] = {}
    for station_id, rows in grouped.items():
        rows = sorted(rows, key=lambda item: parse_float(item.get("time")))
        bikes = [parse_float(row.get("bikes")) for row in rows]
        available = [parse_float(row.get("bikes_available_to_rent")) for row in rows]
        free_racks = [parse_float(row.get("free_racks")) for row in rows]
        latest = rows[-1]
        summaries[station_id] = {
            "status_observations": float(len(rows)),
            "avg_bikes": sum(bikes) / len(bikes) if bikes else 0.0,
            "avg_bikes_available_to_rent": (
                sum(available) / len(available) if available else 0.0
            ),
            "avg_free_racks": sum(free_racks) / len(free_racks) if free_racks else 0.0,
            "latest_bikes_available_to_rent": parse_float(
                latest.get("bikes_available_to_rent")
            ),
        }
    return summaries


def build_station_nodes(
    stations: list[dict[str, str]],
    station_status: list[dict[str, str]],
    city_id: str,
) -> list[dict[str, Any]]:
    """Build one node row per Frankfurt station."""
    city_stations = [row for row in stations if row.get("city_id") == city_id]
    if not city_stations:
        raise FrankfurtBikeSharingError(f"No stations found for city_id={city_id}.")

    status = summarize_station_status(station_status, {row["id"] for row in city_stations})
    nodes = []
    for node_index, row in enumerate(
        sorted(city_stations, key=lambda item: int(parse_float(item.get("id"))))
    ):
        station_id = row["id"]
        station_status_summary = status.get(station_id, {})
        nodes.append(
            {
                "node_index": node_index,
                "station_id": station_id,
                "name": row.get("name", ""),
                "city_id": row.get("city_id", ""),
                "lon": parse_float(row.get("lon")),
                "lat": parse_float(row.get("lat")),
                "bike_racks": parse_float(row.get("bike_racks")),
                "special_racks": parse_float(row.get("special_racks")),
                "terminal_type": row.get("terminal_type", ""),
                "place_type": row.get("place_type", ""),
                "status_observations": station_status_summary.get("status_observations", 0.0),
                "avg_bikes": station_status_summary.get("avg_bikes", 0.0),
                "avg_bikes_available_to_rent": station_status_summary.get(
                    "avg_bikes_available_to_rent", 0.0
                ),
                "avg_free_racks": station_status_summary.get("avg_free_racks", 0.0),
                "latest_bikes_available_to_rent": station_status_summary.get(
                    "latest_bikes_available_to_rent", 0.0
                ),
            }
        )
    return nodes


def haversine_m(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """Great-circle distance in meters."""
    radius_m = 6_371_000.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    )
    return radius_m * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def build_trip_edges(
    trips: list[dict[str, str]],
    nodes: list[dict[str, Any]],
    city_id: str,
) -> list[dict[str, Any]]:
    """Aggregate trips into directed station-to-station edges."""
    station_to_index = {str(node["station_id"]): int(node["node_index"]) for node in nodes}
    edge_stats: dict[tuple[str, str], dict[str, float]] = defaultdict(
        lambda: {"trip_count": 0.0, "distance_sum_m": 0.0, "duration_sum_s": 0.0}
    )

    for row in trips:
        start = row.get("station_id_start", "")
        end = row.get("station_id_end", "")
        if row.get("city_id") != city_id or not start or not end or start == end:
            continue
        if start not in station_to_index or end not in station_to_index:
            continue

        stats = edge_stats[(start, end)]
        stats["trip_count"] += 1.0
        stats["distance_sum_m"] += parse_float(row.get("distance"))
        stats["duration_sum_s"] += parse_float(row.get("duration"))

    edges = []
    for (start, end), stats in sorted(edge_stats.items()):
        trip_count = stats["trip_count"]
        avg_distance_m = stats["distance_sum_m"] / trip_count if trip_count else 0.0
        avg_duration_s = stats["duration_sum_s"] / trip_count if trip_count else 0.0
        edges.append(
            {
                "source": station_to_index[start],
                "target": station_to_index[end],
                "source_station_id": start,
                "target_station_id": end,
                "edge_type": "trip",
                "edge_weight": trip_count,
                "trip_count": trip_count,
                "avg_distance_m": avg_distance_m,
                "avg_duration_s": avg_duration_s,
            }
        )
    return edges


def build_spatial_knn_edges(
    nodes: list[dict[str, Any]],
    k_neighbors: int = DEFAULT_K_NEIGHBORS,
) -> list[dict[str, Any]]:
    """Build undirected spatial k-nearest-neighbor station edges."""
    if k_neighbors < 1:
        raise FrankfurtBikeSharingError("k_neighbors must be at least 1.")
    edges_by_pair: dict[tuple[int, int], dict[str, Any]] = {}

    for source in nodes:
        distances = []
        for target in nodes:
            if source["node_index"] == target["node_index"]:
                continue
            distance_m = haversine_m(
                source["lon"], source["lat"], target["lon"], target["lat"]
            )
            distances.append((distance_m, target))

        for distance_m, target in sorted(distances, key=lambda item: item[0])[:k_neighbors]:
            a = int(source["node_index"])
            b = int(target["node_index"])
            key = (min(a, b), max(a, b))
            edges_by_pair[key] = {
                "source": key[0],
                "target": key[1],
                "source_station_id": nodes[key[0]]["station_id"],
                "target_station_id": nodes[key[1]]["station_id"],
                "edge_type": "spatial_knn",
                "edge_weight": 1.0 / (1.0 + distance_m / 1000.0),
                "trip_count": 0.0,
                "avg_distance_m": distance_m,
                "avg_duration_s": 0.0,
            }
    return [edges_by_pair[key] for key in sorted(edges_by_pair)]


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    """Write dictionaries to CSV."""
    if not rows:
        raise FrankfurtBikeSharingError(f"No rows to write for {path}.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_graph(
    input_dir: Path,
    output_dir: Path,
    city_name: str = CITY_NAME,
    country: str = CITY_COUNTRY,
    k_neighbors: int = DEFAULT_K_NEIGHBORS,
) -> dict[str, Any]:
    """Build and write Frankfurt GCN node and edge tables."""
    cities = read_csv_rows(input_dir / "cities.csv")
    stations = read_csv_rows(input_dir / "stations.csv")
    trips = read_csv_rows(input_dir / "trips.csv")
    station_status = read_csv_rows(input_dir / "station_status.csv")

    city_id = select_city_id(cities, city_name=city_name, country=country)
    nodes = build_station_nodes(stations, station_status, city_id)
    edges = build_trip_edges(trips, nodes, city_id)
    edge_source = "trips"
    if not edges:
        edges = build_spatial_knn_edges(nodes, k_neighbors=k_neighbors)
        edge_source = "spatial_knn"

    nodes_path = output_dir / "frankfurt_bike_sharing_gcn_nodes.csv"
    edges_path = output_dir / "frankfurt_bike_sharing_gcn_edges.csv"
    metadata_path = output_dir / "frankfurt_bike_sharing_gcn_metadata.json"
    write_csv(nodes_path, nodes)
    write_csv(edges_path, edges)

    metadata = {
        "source_repo": SOURCE_REPO,
        "license": "CC BY-NC 4.0",
        "city_name": city_name,
        "city_id": city_id,
        "node_count": len(nodes),
        "edge_count": len(edges),
        "edge_source": edge_source,
        "k_neighbors": k_neighbors if edge_source == "spatial_knn" else None,
        "nodes_csv": str(nodes_path),
        "edges_csv": str(edges_path),
    }
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    return metadata


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a Frankfurt bike-sharing station graph for GCN examples."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "sample",
        help="Directory containing cities.csv, stations.csv, trips.csv, station_status.csv.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data",
        help="Directory for generated GCN CSV files.",
    )
    parser.add_argument(
        "--download-sample",
        action="store_true",
        help="Download small sample CSV files from the source repository before building.",
    )
    parser.add_argument("--k-neighbors", type=int, default=DEFAULT_K_NEIGHBORS)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.download_sample:
        download_sample_files(args.input_dir)
    metadata = build_graph(args.input_dir, args.output_dir, k_neighbors=args.k_neighbors)
    print(
        "Built Frankfurt bike-sharing graph: "
        f"{metadata['node_count']} nodes, {metadata['edge_count']} edges "
        f"from {metadata['edge_source']}."
    )
    print(f"Nodes CSV: {metadata['nodes_csv']}")
    print(f"Edges CSV: {metadata['edges_csv']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
