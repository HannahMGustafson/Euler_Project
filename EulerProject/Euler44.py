def is_penta(num):
	out = (1 + (1+24*num)**0.5)/6
	if out == int(out):
		return True
	else:
		return False

for n in range(1,10000):
	pn1 = n*(3*n-1)/2
	for n in range(1,10000):
		pn2 = n*(3*n-1)/2
		if is_penta(abs(pn1-pn2)) and is_penta(abs(pn1+pn2)):
			print abs(pn1-pn2) 