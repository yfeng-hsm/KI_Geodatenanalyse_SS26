import unittest

from data_loaders.meinrad.src.meinrad_snapshot import (
    MeinRadSnapshotError,
    build_summary,
    flatten_places,
    select_city,
)


class MeinRadSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.payload = {
            "countries": [
                {
                    "name": "meinRad",
                    "domain": "mz",
                    "cities": [
                        {
                            "uid": 755,
                            "name": "Mainz",
                            "num_places": 2,
                            "refresh_rate": "10120",
                            "set_point_bikes": 10,
                            "available_bikes": 4,
                            "return_to_official_only": True,
                            "bike_types": {"188": 3, "295": 1},
                            "places": [
                                {
                                    "uid": 1,
                                    "lat": 50.0,
                                    "lng": 8.2,
                                    "bike": False,
                                    "spot": True,
                                    "name": "Station A",
                                    "number": 42500,
                                    "bikes": 3,
                                    "bikes_available_to_rent": 3,
                                    "bike_racks": 8,
                                    "free_racks": 5,
                                    "maintenance": False,
                                    "bike_types": {"188": 2, "295": 1},
                                    "bike_list": [{"number": "1"}, {"number": "2"}, {"number": "3"}],
                                },
                                {
                                    "uid": 2,
                                    "lat": 50.1,
                                    "lng": 8.3,
                                    "bike": True,
                                    "spot": False,
                                    "name": "BIKE 1",
                                    "bikes": 1,
                                    "bikes_available_to_rent": 1,
                                    "bike_list": [{"number": "1"}],
                                },
                            ],
                        }
                    ],
                }
            ]
        }

    def test_select_city_finds_mainz(self):
        country, city = select_city(self.payload)

        self.assertEqual(country["domain"], "mz")
        self.assertEqual(city["name"], "Mainz")

    def test_select_city_raises_for_missing_city(self):
        with self.assertRaises(MeinRadSnapshotError):
            select_city({"countries": []})

    def test_build_summary_counts_place_types(self):
        country, city = select_city(self.payload)
        summary = build_summary(country, city, "2026-07-12T10:00:00+00:00")

        self.assertEqual(summary["places_returned"], 2)
        self.assertEqual(summary["station_places"], 1)
        self.assertEqual(summary["floating_bike_places"], 1)
        self.assertEqual(summary["available_bikes"], 4)

    def test_flatten_places_omits_bike_identifiers(self):
        country, city = select_city(self.payload)
        rows = flatten_places(country, city, "2026-07-12T10:00:00+00:00")

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["bike_count_from_list"], 3)
        self.assertNotIn("bike_list", rows[0])
        self.assertNotIn("bike_numbers", rows[0])


if __name__ == "__main__":
    unittest.main()
