import configparser
import requests
import sys
import json
import weather_data_parsing


url = "https://api.openweathermap.org/data/2.5/forecast?id=3369157&appid=e141245f76fbb881dfba64a59a75ac71"
r = requests.get(url,verify=False)
print(r)
f = open('weather.json','w')
json.dump(r.json(),f,indent=4);
f.close()
exec(open('weather_data_parsing.py').read())
