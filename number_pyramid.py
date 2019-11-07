
numbers = 5

def num_pyramid_one(n):
	# Number of rows	
	for i in range(1, n+1):

		# Stars
		for j in range(1, i+1):
			print(i, end = " ")

		# New Line
		print("\r")

num_pyramid_one(numbers)


def num_pyramid_two(n):
	
	num = 1
		
	# Number of rows	
	for i in range(1, n+1):

		# Stars
		for j in range(1, i+1):
			print(num, end = " ")
			num = num + 1;

		# New Line
		print("\r")

num_pyramid_two(numbers)