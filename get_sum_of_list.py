# Get Sum of List Items
def get_sum_of_list(list):
	# Inbuilt function
	# return sum(list)
	sum = 0
	for value in list:
		sum = sum + value
	return sum

list = [45, 42, 12, 41]
print(get_sum_of_list(list))