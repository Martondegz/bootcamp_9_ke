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






def reverse_string(string):
  
  # first check for string length or Null
  if len(string) == 0:
    return None
  
  # empty list initialized to store elements of reversed strings
  str_list = []
  
  # loop through string length and applying slicing, each element is reversed
  for i in range(len(string)):
    
    # reversed elements are added to str_list
    str_list.append(string[len(string)-i-1])
  
  # str_list convert to string and stored in variable str2
  str2 = ''.join(str_list)
  #print str2
  
  # check on whether reverse is even or like original string (palindrome)
  if str2 == string:
    return True

  else: 
    return str2
