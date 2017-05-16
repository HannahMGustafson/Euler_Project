def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

primecount = 0
num = 2
while primecount < 10001:
	if is_prime(num):
		primecount += 1
		print num
	num += 1