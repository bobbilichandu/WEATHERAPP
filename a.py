import json,requests
from location import loc

def wdata(val):
# Automatically geolocate the connecting IP
    lo=loc(val)
    lat=lo[0]
    lan=lo[1]
    url="https://weather.cit.api.here.com/weather/1.0/report.json?product=observation&latitude="+str(lat)+"&longitude="+str(lan)+"&oneobservation=true&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg"
    f = requests.get(url)
    weather_data = f.json()
    observations=weather_data['observations']
    a=observations['location']
    aa=a[0]
    final_obs=aa['observation']
    
    final_observation=final_obs[0]
    return final_observation
    
    
