


def fibby(n):
	
	# initialize two counter vaiables
	a, b = 0, 1
	# create a new list to hold sequence
	my_list = [1]
	# loop through range of 0 and input
	for i in range(0,n):
		
		# fibonacci sequence moderator
		# num is a placeholder for the original value of a
		num = a
		# a is assigned the value of b in the addition via the sequence
		a = b
		# b is assigned the value of the original 'a' and it's pre-value digit
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


print fibbz(10)