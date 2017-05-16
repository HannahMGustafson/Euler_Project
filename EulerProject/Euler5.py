val = 0
num = 2*3*5*7*11*13*17*19*20



while val == 0:
	num += 20
	print num
	remain = []
	for x in range(2, 21):
		remain.append(num%x)
	if sum(remain) == 0:
		print 'You found it!!'
		val = 1		



