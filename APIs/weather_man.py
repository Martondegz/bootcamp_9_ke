import json
import urllib3
from pprint import pprint

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CONSUMER_KEY = '2bc3e79bb974a007818864813f53fd35'

def weather_man(city_name):
	http = urllib3.PoolManager()
	main = {}
	
	for city in city_name:
		main_data = {}
		
		r = http.request('GET', BASE_URL, 
			fields={
			'q': city_name,
			'APPID': CONSUMER_KEY,
			'units':'metrics',
			})

		response = json.loads(r.data.decode('utf-8'))
		main_data.update(response['main'])
		main[city] = main_data

	pprint(main)


weather_man(['Kampala', 'Nairobi', 'Lagos'])
