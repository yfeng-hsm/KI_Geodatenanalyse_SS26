import unittest

from data_loaders.frankfurt_bike_sharing.src.frankfurt_bike_sharing_gcn import (
    build_spatial_knn_edges,
    build_station_nodes,
    build_trip_edges,
    select_city_id,
)


class FrankfurtBikeSharingGcnTests(unittest.TestCase):
    def setUp(self):
        self.cities = [
            {"id": "482", "name": "Frankenthal (Pfalz)", "country": "DE"},
            {"id": "8", "name": "Frankfurt", "country": "DE"},
        ]
        self.stations = [
            {
                "id": "101",
                "city_id": "8",
                "name": "Station A",
                "lon": "8.68",
                "lat": "50.11",
                "bike_racks": "10",
                "special_racks": "1",
                "terminal_type": "free",
                "place_type": "0",
            },
            {
                "id": "102",
                "city_id": "8",
                "name": "Station B",
                "lon": "8.69",
                "lat": "50.12",
                "bike_racks": "8",
                "special_racks": "0",
                "terminal_type": "sign",
                "place_type": "0",
            },
            {
                "id": "103",
                "city_id": "8",
                "name": "Station C",
                "lon": "8.70",
                "lat": "50.13",
                "bike_racks": "6",
                "special_racks": "0",
                "terminal_type": "",
                "place_type": "0",
            },
        ]
        self.station_status = [
            {
                "station_id": "101",
                "time": "1661530441",
                "bikes": "2",
                "bikes_available_to_rent": "2",
                "free_racks": "8",
            },
            {
                "station_id": "101",
                "time": "1661531341",
                "bikes": "4",
                "bikes_available_to_rent": "3",
                "free_racks": "6",
            },
        ]

    def test_select_city_id_finds_frankfurt_not_frankenthal(self):
        self.assertEqual(select_city_id(self.cities), "8")

    def test_build_station_nodes_adds_status_features(self):
        nodes = build_station_nodes(self.stations, self.station_status, "8")

        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0]["station_id"], "101")
        self.assertEqual(nodes[0]["status_observations"], 2.0)
        self.assertEqual(nodes[0]["avg_bikes_available_to_rent"], 2.5)

    def test_build_trip_edges_aggregates_station_trips(self):
        nodes = build_station_nodes(self.stations, self.station_status, "8")
        trips = [
            {
                "city_id": "8",
                "station_id_start": "101",
                "station_id_end": "102",
                "distance": "1000",
                "duration": "600",
            },
            {
                "city_id": "8",
                "station_id_start": "101",
                "station_id_end": "102",
                "distance": "1200",
                "duration": "660",
            },
            {
                "city_id": "482",
                "station_id_start": "101",
                "station_id_end": "102",
                "distance": "9999",
                "duration": "9999",
            },
        ]

        edges = build_trip_edges(trips, nodes, "8")

        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0]["trip_count"], 2.0)
        self.assertEqual(edges[0]["avg_distance_m"], 1100.0)

    def test_build_spatial_knn_edges_creates_edges_without_trips(self):
        nodes = build_station_nodes(self.stations, self.station_status, "8")
        edges = build_spatial_knn_edges(nodes, k_neighbors=1)

        self.assertGreaterEqual(len(edges), 2)
        self.assertEqual({edge["edge_type"] for edge in edges}, {"spatial_knn"})


if __name__ == "__main__":
    unittest.main()
