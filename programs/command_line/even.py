"""Even checker using docopt

Usage:
  even.py <operation> <num1>
  even.py (-h | --help)

Arguments
  num1 First Number

Options:
  -h --help     Show this screen.

"""

from docopt import docopt

if __name__ == '__main__':
	args = docopt(__doc__, version='Calculator with docopt')
	functions = {
	'even' : lambda num1:  "odd" if num1 % 2 else "even",
	
	}

	print functions[args['<operation>']](int(args['<num1>']))
