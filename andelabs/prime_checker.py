"""
Create a class PrimeChecker(number), that takes in a string argument.
When the instance of the class is called with .is_prime() it should return true
if number is a prime number and false if it isn't.
"""



class PrimeChecker(object):
  
  # initialize class constructor with is_prime() var num
  def __init__(self, number= ''):
    self.number = number
    # return number
  
  # class metod is_prime with a class argument which in turn calls 'number'
  def is_prime(self):
    # first check which checks whether the string is empty and returns False
    if self.number == '':
      return False
      
    
    else:
      # loop through from 2(prime) to the input specified (number)
      for i in range(2,int((self.number))):
        # prime check for whether remainder is a 0 which in turn returns False
        if int(self.number) % i == 0:
          return False
      # returns True if number is prime and if remainder is not equal to 0    
      return True
