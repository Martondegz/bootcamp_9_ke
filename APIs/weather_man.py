import urllib2, urllib, json
import urllib3




def weather_man(city_name):
	http = urllib3.PoolManager()
	base_url = "http://api.openweathermap.org/data/2.5/weather"
	consumer_key = '2bc3e79bb974a007818864813f53fd35'
	city_name = city_name
	r = http.request('GET', base_url, 
		fields={
		'q': city_name,
		'APPID': consumer_key,
		'units':'metrics',
		})

	dee =json.loads(r.data.decode('utf-8'))

	print dee


weather_man('Lagos')