class WeatherObject(object):
    def __init__(self, weather_data):
        self._weather_data = weather_data

    def last_build_date(self):
        return self._weather_data['lastBuildDate']

    def title(self):
        return self._weather_data['title']

    def description(self):
        return self._weather_data['description']

    def language(self):
        return self._weather_data['language']

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

    def print_obj(self):
        return self._weather_data
