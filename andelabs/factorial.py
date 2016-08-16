"""
Have a function factorial(number), take the number parameter been passed
and return the factorial of it.
For example: if number is 4, it should return (4 * 3 * 2 * 1) which is 24.

"""

# factorial done using recursion

def factorial(number):

  # first check whether input is equal to 1 since factorial entails product from 1
	if number == 1:

		return number
	else:
      # input will be multiplied by the method's call until the base case (1) is 
      # achieved thus if input is 10, result will be (10*9*8*7*6*5*4*3*2*1) where
      # each value comes as a recurring method call

	return number*factorial(number-1)

