def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val


test_num = 	600851475143
is_prime_factor = []
for x in range(test_num,2,-1):
	if test_num%x == 0 and is_prime(x):
		is_prime_factor = x
		break
		

print is_prime_factor
