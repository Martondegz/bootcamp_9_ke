"""
Prime Numbers
"""

"""
prime checks whether a number is prime and returns either true or false
"""

"""
prime_list appends all primes in a list and returns the list
"""

def prime(x):
	if x < 2:
		return False

	else:
		for i in range(2,x):
			if x % i == 0:
				return False
		return True

# print prime(100)


def prime_list(b):
	primes = []
	for x in range(2,b):
		if prime(x):
			primes.append(x)
			return primes
		else:
			print 'input a prime number'




print prime_list(100)