"""
input returns dictionary mapping word to it's occurence value
"olly olly in come free"
returns { olly:2, in:1, come:1, free:1 }

"""

# loop through and check against elements for equality
# create empty dictionary

def words(input):

	# first check splits the input thus identifying the whitespaces
	data = input.split()

	# print data

	# an empty dictionary to hold the final value
	data_dict ={}

	# this set contains the unique values present in the list data
	unique_values = set(data)
	# print unique_values

	# the loop identifies all the unique elements and checks against data list
	for x in unique_values:

		count = 0

		# second loop to comapare first loop variable
		for y in data:

			# this check compares the looping variable
			if x  == y:
				count = count + 1

				# the check below identifies an integer in a string, if true the string is casted to an integer
				if x.isdigit() == True:

						x = int(x)
						
		data_dict[x] = count

	return data_dict



print words('testing 1 2 testing')