import requests


class Weather(object):
    URL = 'http://query.yahooapis.com/v1/public/yql'

    def lookup(self, woeid):
        url = '%s?q=select * from weather.forecast where woeid = %s&format=json' % (self.URL, woeid)
        results = self._call(url)
        return results

    def search(self, location):
        url = "%s?q=select* from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s')&format=json" % (
            self.URL, location)
        results = self._call(url)
        return results

    def _call(self, url):
        res = requests.get(url).json()
        return res
