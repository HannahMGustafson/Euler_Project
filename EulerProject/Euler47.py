def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val



def prime_fact(num):
	pf = []
	temp = num
	for x in pl:
		while temp%x == 0:
			temp = temp/x
			if x not in pf:
				pf.append(x)
		if x == 1:
			break
	return len(pf)

pl = []
for x in range(2,100000):
	if is_prime(x):
		pl.append(x)

y = False
n = 10
while y is False:
	if prime_fact(n) == 4:
		four_ct += 1
	else:
		four_ct = 0
	if four_ct == 4:
		print n-3
		break
	if n%1000 == 0:
		print n
	n += 1
	