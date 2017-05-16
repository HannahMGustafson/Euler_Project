import math
def factorial_digs(my_str):
	my_sum = 0
	for y in my_str:
		my_sum += math.factorial(int(y))
	return my_sum

for x in range(3,1000000):
	if factorial_digs(str(x)) == x:
		print x
