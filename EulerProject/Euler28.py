highest = 1
inc = 2
spiral=[1]
for n in range(3,1002,2):
	for x in range(highest+inc,n**2+1,inc):
		spiral.append(x)
	inc += 2
	highest = max(spiral)
print sum(spiral)
