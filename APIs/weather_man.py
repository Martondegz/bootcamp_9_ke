import json
import urllib3
from pprint import pprint

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CONSUMER_KEY = '2bc3e79bb974a007818864813f53fd35'


def weather_man(city_name):
	http = urllib3.PoolManager()
	
	header = 'city'.ljust(15)
	header += 'humidity'.ljust(15)
	header += 'temperature'.ljust(15)
	header += 'description'.ljust(15)+'\n'
	header += '='*55
	print header

	for city in city_name:
		
		r = http.request('GET', BASE_URL, 
			fields={
			'q': city,
			'APPID': CONSUMER_KEY,
			'units':'metric',
			})

		response = json.loads(r.data.decode('utf-8'))

		output = response['name'].ljust(15)
		output += str(response['main']['humidity']).ljust(15)
		output += str(response['main']['temp']).ljust(15)
		output += str(response['weather'][0]['description']).ljust(15)
		
		
		print output 
	


weather_man(['Kampala', 'Nairobi', 'Lagos', 'New York','Madrid'])
