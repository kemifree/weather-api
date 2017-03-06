import requests


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
        if int(results['query']['count']) > 0:
            obj.append(WeatherObject(results['query']['results']['channel']))
            wo = WeatherObject(results['query']['results']['channel'])
            return wo
        else:
            print 'No results found.'


class WeatherObject(object):
    def __init__(self, weather_data):
        self._weather_data = weather_data

    def description(self):
        return self._weather_data['description']

    def astronomy(self):
        return self._weather_data['astronomy']

    def atmosphere(self):
        return self._weather_data['atmosphere']

    def image(self):
        return self._weather_data['image']

    def condition(self):
        return self._weather_data['item']['condition']

    def forecast(self):
        return self._weather_data['item']['forecast']

    def latitude(self):
        return self._weather_data['item']['lat']

    def longitude(self):
        return self._weather_data['item']['lng']

    def location(self):
        return self._weather_data['location']

    def units(self):
        return self._weather_data['units']

    def wind(self):
        return self._weather_data['wind']


if __name__ == '__main__':
    weather = Weather()
    search = weather.search('dublin')
    condition = search.condition()
    print condition['text']
