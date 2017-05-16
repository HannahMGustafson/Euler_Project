def sum_factors(num):
	summation = 0
	for x in range(1,num/2 + 1):
		if num%x == 0:
			summation += x
	return summation


amicable = []
for x in range(1,10000):
	temp = sum_factors(x)
	temp2 = sum_factors(temp)
	if x == temp2:
		if temp not in amicable and temp != temp2:
			amicable.append(temp)
		if temp2 not in amicable and temp != temp2:
			amicable.append(temp2)
print amicable
print sum(amicable)