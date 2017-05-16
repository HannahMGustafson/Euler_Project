
max_len = 0
for x in range(2,1001):
	rem = []
	remain = 10
	while remain != 0:
		# Ensures that the number is greater than the divisor
		while remain < x: 
			remain *= 10
		remain = (remain)%x
		
		if remain in rem:
			rem.append(remain)
			break
		else:
			rem.append(remain)
	if len(rem)>max_len:
		max_len = len(rem)
		print len(rem)
		print x


