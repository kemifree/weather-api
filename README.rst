weather-api
===========

A Python wrapper for the Yahoo Weather XML RSS feed.

Install
-------

::

    pip install weather-api

Examples
--------

.. code:: python


    from weather import Weather
    weather = Weather()

    # Look up WOEID via http://weather.yahoo.com.

    lookup = weather.lookup(560743)
    condtion = lookup.condition()
    print condition['text']

    # Lookup via location name.

    location = weather.lookup_by_location('dublin')
    condition = location.condition()
    print condition['text']
