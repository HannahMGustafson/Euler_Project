import itertools

def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

pd = '12345678'
val = 0
while val == 0:
	temp = itertools.permutations(pd)
	vals = [int(''.join(x)) for x in temp]
	for x in vals[::-1]:
		if is_prime(int(x)):
			val = x
			print x
			break
	pd = pd[:-1]
