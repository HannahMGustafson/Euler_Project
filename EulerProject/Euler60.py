def is_prime(num):
	val = True
	if num == 1:
		return False
	if num == 2:
		return True
	for x in range(3,int(num**0.5)+1,2):
		if num%x == 0:
			val = False
			break
	return val


prime_list = []
for x in range(1,100000):
	if is_prime(x):
		prime_list.append(x)


for indi, i in enumerate(prime_list):
	for indj, j in enumerate(prime_list[indi+1:]):
		for indk, k in enumerate(prime_list[indj+1:]):
			for l in prime_list[indk+1:]:
				if int(str(i)+str(j)) in prime_list and\
				int(str(i)+str(k)) in prime_list and\
				int(str(i)+str(l)) in prime_list:
					print [i,j,k,l]
					break

