def pentnum(num):
	out = (1 + (1+24*num)**0.5)/6
	if out == int(out):
		return True
	else:
		return False

def trinum(num):
	out = (-1 + (1+8*num)**0.5)/2
	if out == int(out):
		return True
	else:
		return False

def hexnum(num):
	out = (1 + (1+8*num)**0.5)/4
	if out == int(out):
		return True
	else:
		return False

for n in range(286, 1000000):
	val = n*(n+1)/2
	if pentnum(val) and hexnum(val):	
		print val
		break

