p = []
for a in range(1,500):
	for b in range(1,500):
		c = (a*a+b*b)**0.5
		if int(c) == c and a+b+c <= 1000:
			p.append(a+b+c)

max_p = 0
for x in range(1,1001):
	if p.count(x)>max_p:
		max_p = p.count(x)
		print x
		print p.count(x)



