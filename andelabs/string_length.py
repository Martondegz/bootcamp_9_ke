"""
You are presented with a string or a collection of strings

Your function should return the length of the string, or strings in a list

['Fairy', 'tale'] should return [5, 4]

'C-sharp' should return [7]
"""


def string_length(string):
	# create a new empty list to hold sum
	list_1 = []

	# first check where input is compared to a string
	if type(string) == str:

		# if test is passed the value's length is appended to list_1
		list1.append(len(string))
		return list1
	# second check where input is compared to a list	
	elif type(string) == list:
		# a loop through list items
		for x in string:
			# list element length is appended to list_1
			list1.append(len(x))
			return list1


# Method 2 check for strings

def string_length(x):
  
  	# if input is list, convert elements to string
	str1 = ''.join(x)
	
	# a new list for length of strings
	str_length = []
	
	# a vaiable for str1's length
	length =  len(str1)
	
	# str1's length is appended to str_length list and returned
	str_length.append(length)
	return str_length