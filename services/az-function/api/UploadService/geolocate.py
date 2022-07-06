import requests
import logging
from .secret import atlas_url

def geolocate(place: str) -> tuple:
  search_url = '%s&query=%s' % (atlas_url, place)
  try:
    response = requests.get(search_url).json()
    lat = response['results'][0]['position']['lat']
    lon = response['results'][0]['position']['lon']
    return (lat, lon)
  except Exception as e:
    print("Failed to retrieve geolocation")
    logging.info("Failed to retrieve geolocation")
    raise e

if (__name__ == '__main__'):
  print(geolocate('Helsinki'))