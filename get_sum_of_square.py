# Sum of squares
def get_sum_of_square(n): 
	sum = 0
	for value in range(1, n+1):
		sum = sum + (value * value)
	return sum

print(get_sum_of_square(4))