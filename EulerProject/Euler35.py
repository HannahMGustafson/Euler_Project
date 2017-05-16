def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

def rotate_digs(num):
	val = str(num)
	for x in range(1,len(val)+1):		
		if is_prime(int(val)) is False:
			return False
			break
		val = val[1:] + val[:1]
		if x == len(val):
			return True


cprimes = []
for x in range(2,1000000):
	if rotate_digs(x) is True:
		cprimes.append(x)
print len(cprimes)

