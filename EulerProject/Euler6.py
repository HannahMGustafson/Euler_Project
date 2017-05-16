sumosq = 0
for x in range(1,101):
	sumosq += x**2
	sqosum = sum(range(1,x+1))**2
print sqosum-sumosq
