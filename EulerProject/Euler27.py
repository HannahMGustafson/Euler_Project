def is_prime(num):
	val = True
	if num <= 0:
		val = False
	else:
		for x in range(2,int(num**0.5)+1):
			if num%x == 0:
				val = False
				break
	return val


max_count = 0
for a in range(-1000, 1000):
	for b in range(-1000, 1001):
		count= 0
		for n in range(0,100):
			temp = n**2+a*n+b
			if is_prime(temp) is True:
				count += 1
			else:
				break
		if count > max_count:
			max_count = count
			print count
			print a*b