def check_pd(x,y,z):
	all_nums = str(x)+str(y)+str(z)
	if str(0) in all_nums:
		return False
	for n in range(1,10):
		if all_nums.count(str(n)) != 1:
			return False
	return True 

summation = 0
pds = []
for x in range(2,100):
	if '0' not in str(x) and x%11 != 0:
		for y in range(1,10000):
			z = x*y
			if check_pd(x,y,z) is True:
				if z not in pds:
					pds.append(z)
					summation += z
					print summation