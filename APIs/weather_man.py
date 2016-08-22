import json
import urllib3
from pprint import pprint


def weather_man(city_name):
	http = urllib3.PoolManager()
	base_url = "http://api.openweathermap.org/data/2.5/weather"
	consumer_key = '2bc3e79bb974a007818864813f53fd35'
	
	main = {}
	# sys = {}
	for city in city_name:
		main_data = {}
		# sys_data = {}
		r = http.request('GET', base_url, 
			fields={
			'q': city_name,
			'APPID': consumer_key,
			'units':'metrics',
			})

		response = json.loads(r.data.decode('utf-8'))
		main_data.update(response['main'])
		# sys_data.update(response['sys'])
		# sys[city] = sys_data
		main[city] = main_data

	pprint(main)
	# pprint(sys)


weather_man(['Kampala', 'Nairobi', 'Lagos'])
