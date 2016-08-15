"""
Prime Numbers
"""



def prime(x):
	if x < 2:
		return False

	else:
		for i in range(2,x):
			if x % i == 0:
				return False
		return True

print prime(100)