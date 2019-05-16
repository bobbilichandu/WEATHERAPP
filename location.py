import requests
import json

# Automatically geolocate the connecting IP
f = requests.get('https://weather.cit.api.here.com/weather/1.0/report.json?product=observation&latitude=12.9487925&longitude=77.6904785&oneobservation=true&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg')
location = f.json()
print(location)
