import googlemaps
from datetime import datetime

with open('gmapsAPIkey.txt', 'r') as f:
        gmapsAPIkey = f.read().strip()
gmaps = googlemaps.Client(key=gmapsAPIkey)

# Geocoding an address
geocode_result = gmaps.geocode('UniversitĂ© de Montpellier, France')
print(len(geocode_result))
print(geocode_result[0]['geometry']['location'])
