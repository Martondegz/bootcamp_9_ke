"""
You are to write a function, reverse_string(string), that returns the reverse of the 
string provided. If the reverse of the string is the same as the original string,
as in the case of palindromes, return true instead.

"""


def reverse_string(string):

	# check whether input is equal to reverse
	if string[::-1] == string:
		return True

	# check for whether the input is empty or Null
	elif string == '':
		return None

	# return the reverse if previous checks fail	
	else:
		return string[::-1]






