"""
You are presented with two arrays, all containing positive integers.
One of the arrays will have one extra number, see below:

[1,2,3] and [1,2,3,4] should return 4

[4,66,7] and [66,77,7,4] should return 77

"""



def find_missing(a, b):
# 	a = [1,2,3]
# 	b = [1,2,3,4]
  # this is the variable that holds the unique number
  # between the two inputed lists
	holder = 0
	
	# first check of the input length which facilitates comparison
	if len(a) < len(b):
	  # sets allow arithmetic ops on lists thus list1 holds the unique element
		list1 = (set(b) - set(a))
		# this step removes the emenet from the set list1 to variable holder
		holder = list1.pop()
		return holder

  # second check on list lengths
	elif len(b) < len(a):
	  # list2 holds the final and unique value and this is
	  # based on the second size check
		list2 = (set(a) - set(b))
		
		holder = list2.pop()
		return holder
	else:
	  return 0


# print list_entries()