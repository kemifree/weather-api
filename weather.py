import requests
import pprint


class Weather(object):
    URL = 'http://query.yahooapis.com/v1/public/yql'

    def lookup(self, woeid):
        url = '%s?q=select * from weather.forecast where woeid = %s&format=json' % (self.URL, woeid)
        results = self._call(url)
        return results

    def search(self, location):
        url = "%s?q=select* from weather.forecast " \
              "where woeid in (select woeid from geo.places(1) where text='%s')&format=json" % (self.URL, location)
        results = self._call(url)
        return results

    @staticmethod
    def _call(url):
        obj = []
        results = requests.get(url).json()
        if results['query']['count'] > 0:
            obj.append(WeatherObject(results['query']['results']['channel']))
        pprint.pprint(results)
        return obj


class WeatherObject(object):
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def description(self):
        return self.weather_data['description']

    def astronomy(self):
        return self.weather_data['astronomy']

    def atmosphere(self):
        return self.weather_data['atmosphere']

    def image(self):
        return self.weather_data['image']

    def condition(self):
        return self.weather_data['item']['condition']['text']

    def forecast(self):
        return self.weather_data['item']['forecast']

    def latitude(self):
        return self.weather_data['item']['lat']

    def longitude(self):
        return self.weather_data['item']['lng']

    def location(self):
        return self.weather_data['location']

    def units(self):
        return self.weather_data['units']

    def wind(self):
        return self.weather_data['wind']
