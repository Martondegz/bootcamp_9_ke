"""
You are to write a function, reverse_string(string), that returns the reverse of the 
string provided. If the reverse of the string is the same as the original string,
as in the case of palindromes, return true instead.

"""


# def reverse_string(string):
  # if reversed(string) == string:
  #   print string, reversed(string)
  #   return reversed(string)
  # elif string == '':
  #   return None
  # else:
  #   new_string = reversed(string)
  #   return new_string


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
