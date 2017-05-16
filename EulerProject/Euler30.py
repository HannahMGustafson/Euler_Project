nums = []

for x in range(1,000000):
	temp2 = 0
	temp =  str(x)
	# fix code to deal with length of numbers
	for y in temp:
		temp2 += int(y)**5
	if x == temp2:
		nums.append(x)
print sum(nums)

