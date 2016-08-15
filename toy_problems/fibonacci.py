


def fibby(n):
	
	# initialize two vaiables
	a, b = 0, 1
	# create a new list to hold sequence
	my_list = []
	# loop through range of 0 and input
	for i in range(0,n):
		
		# fibonacci sequence moderator
		num = a
		a = b
		b = num + b

		# added sequence values to list
		my_list.append(b)
	return my_list

print fibby(20)




# Recursion

def fibbz(n):
	if n == 1 or n == 2:
		return n

	else:
		return fibbz(n-1)+fibbz(n-2)


fibbz(10)