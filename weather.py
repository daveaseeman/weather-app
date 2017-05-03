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
    current_summary = current_forecast.summary
    current_temperature = current_forecast.temperature
    forecast = "{} and {}° at {}".format(
        current_summary,
        current_temperature,
        address
    )
    return forecast
