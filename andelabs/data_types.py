"""
Define a function called data_type, to take one argument.
Compare and return results, based on the argument supplied to the function. 
Complete the test to produce the perfect function that accounts for all expectations.

For strings, return its length.
For None return string 'no value'
For booleans return the boolean
For integers return a string showing how it compares to hundred e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
For lists return the 3rd item, or None if it doesn't exist

"""
def data_type(y):
	# check for strings
  if type(y) == str:
  	# hold is a variable that holds the length of y
    hold = len(y)
    return hold
  # check for boolean with a return value of the boolean
  elif type(y) == bool:
    return y
  # check for integer where the int is less than 100
  elif type(y) == int and y < 100:
    return 'less than 100'
  # check for integer where the int is greater than 100
  elif type(y) == int and y > 100:
    return 'more than 100'
  # check for integer where the int is equal to 100
  elif type(y) == int and y == 100:
    return 'equal to 100'
  # check for list
  elif type(y) == list:
  	# check for the list size to avoid 'index out of bound exception'
    if len(y) >= 3:
      return y[2]
  else:
    return 'no value'