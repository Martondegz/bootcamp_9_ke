"""
You are to create a Car class that can be used to instantiate various vehicles.

It takes in arguments that depict the type, model, and name of the vehicle, provided they are set.

Let the test guide you to building your Car boiler-plate.


atttributes include: name, model, num_of_doors, num_of_wheels, parked_speed, moving_speed

methods include: is_saloon(), drive(), 
"""




class Car(object):
	
	def __init__(self, name, model, type, speed=0, num_of_doors=0, num_of_wheels=0, parked_speed = 0, moving_speed = 0):
		super(Car, self).__init__()
		self.name = name
		self.model = model
		self.type = type
		self.speed = speed
		self.num_of_doors = num_of_doors
		self.num_of_wheels = num_of_wheels
		self.parked_speed = parked_speed
		self.moving_speed = moving_speed
		
	# check for car type
	def is_saloon(self, type):
		if type == self.saloon:
			return 'saloon'
		return 'trailer'

	def drive(self, speed):
		if speed > 0:
			return speed
		return ' {0} should have speed {1} km/h until you put `the pedal to the metal`'.format(name, speed)