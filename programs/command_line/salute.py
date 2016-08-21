"""Salute.

Usage:
  salute.py hello <name>
  salute.py goodbye <name>
  salute.py even [<num>]
  salute.py (-h | --help)

Options:
  -h --help     Show this screen.

"""
from docopt import docopt

def hello(name):
	print('Hello, {0}'.format(name))


def goodbye(name):
	print('Goodbye, {0}'.format(name))

def even(num):
	if num % 2 == 0:
		print('Even!!')
	else:
		print('Odd!...damn!')


if __name__ == '__main__':
	arguments = docopt(__doc__)

	if arguments['hello']:
		hello(arguments['<name>'])

	elif arguments['goodbye']:
		goodbye(arguments['<name>'])

	elif arguments['even']:
		even(arguments['<name>'])
