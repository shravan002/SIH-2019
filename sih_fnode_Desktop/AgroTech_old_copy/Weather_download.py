import configparser
import requests
import sys
import json

#def get_weather():
	
	#if(r.json() == null ):
	#print("Error Occured")
	
	#return r.json()


url = "https://api.openweathermap.org/data/2.5/forecast?id=3369157&appid=e141245f76fbb881dfba64a59a75ac71"
r = requests.get(url)
f = open('weather.json','w')
json.dump(r.json(),f,indent=4);
f.close()
execfile("weather_data_parsing.py")

