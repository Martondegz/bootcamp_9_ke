
class StringSplosion(object):

	def __init__(self, string):
		super(StringSplosion, self).__init__()
		self.string = string

	def string_splosion(self):
		lister = []
		for i in range(1, len(self.string)):
			lister.append(self.string[:1])
			for x in range(lister):
			  new_data = []
			  new_data.append(lister[x]+lister[x])
		return new_data