def coll(num):
	if num%2 == 0:
		num = num/2
	elif num%2 != 0:
		num = num*3 + 1
	return num

maxcount = 0
for x in range(1,1000001):
	count = 1
	num = x
	while num != 1:
		num = coll(num)
		count += 1
	if count > maxcount:
		maxcount = count
		maxnum = x
		print maxnum


