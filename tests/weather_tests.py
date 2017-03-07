import unittest
from weather import Weather


class WeatherTests(unittest.TestCase):
    def test_lookup(self):
        w = Weather()
        data = w.lookup(woeid=560743)
        self.assertTrue('Dublin' in data.description())

    def test_search(self):
        w = Weather()
        data = w.lookup_by_location('Dublin')
        self.assertTrue('Dublin' in data.description())
