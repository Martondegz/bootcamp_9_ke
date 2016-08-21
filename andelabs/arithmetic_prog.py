from __future__ import division

"""
You are required to check if the array passed as an argument is arithmetic,
geometric, neither arithmetic nor geometric in progression or 
if the array is empty.

For arithmetic progressions, return Arithmetic
For geometric progressions, return Geometric
For neither of the above, return -1
For an empty array, return 0


"""





# def arith_geo(x):

# 	# first check for an empty list
# 	if len(x) == 0:
# 		return 0

# 	first_element = x[0]
# 	# print first_element

# 	second_element = x[1]
	

# 	arith = x[1] - x[0]

# 	geo = x[1] / x[0]

# 	arith_temp = range(first, last, arith_diff)

# 	arith_temp.append(last)

# 	geo_temp = range(first, last, geo_diff)

# 	geo_temp.append(last)


# 	if x == arith_temp:
# 		return 'Arithmetic'
# 	elif x == geo_temp:
# 		return 'Geometric'

# arith_geo([1,2,3,4])



def arith_geo(x):

	# first check for an empty list
	if len(x) == 0:
		return 0

	for i in range(len(x) - 2):

		midd = x[1] - x[0]
		mult = x[0] / x[1]
		
		if x[i] * x[i + 2] == x[i + 1]**2:
			return 'Geometric'

	for y in range(len(x)-1):
		
		if x[y + 1] - x[y] == midd:
			return 'Arithmetic'

	return -1
	 
