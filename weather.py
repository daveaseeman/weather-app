# -*- coding: utf-8 -*-
# import sys
import os
import forecastio
from geopy.geocoders import Nominatim

# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

# reload(sys)
# sys.setdefaultencoding('utf8')


def get_forecast(address):
    api_key = os.environ['API_KEY']
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    lat = location.latitude
    lng = location.longitude
    forecast = forecastio.load_forecast(api_key, lat, lng)
    current_forecast = forecast.currently()
    current_condition = current_forecast.icon
    current_temperature = current_forecast.temperature
    current_wind = current_forecast.windSpeed
    current_bearing = current_forecast.windBearing
    current_visibility = current_forecast.visibility
    forecast = "Currently {} and {}°F, with winds {}mph {}NNE, visibility {} miles at {}".format(
        current_condition.lower(),
        current_temperature,
        current_wind,
        current_bearing,
        current_visibility,
        address
    )
    return forecast
