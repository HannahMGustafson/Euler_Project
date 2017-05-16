def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

summation = 2
for x in range(3,2000000,2):
	if is_prime(x):
		summation += x
print summation