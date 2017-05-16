def is_prime(num):
	val = True
	if num == 1:
		return False
	if num == 2:
		return True
	for x in range(3,int(num**0.5)+1,2):
		if num%x == 0:
			val = False
			break
	return val

def check_ratio(new_vals, yc):
	for x in new_vals:
		if is_prime(x):
			yc += 1
	return (yc)


highest = 1
inc = 2
spiral=[1]
yc = 0

for n in range(3,100000,2):
	temp = []
	for x in range(highest+inc,n**2+1,inc):		
		spiral.append(x)
		temp.append(x)
	(yc) = check_ratio(temp, yc)
	inc += 2
	highest = max(spiral)
	val = float(yc)/float(len(spiral))
	if n%1001 == 0:
		print val	
	if val<0.10:
		print inc-1
		break

