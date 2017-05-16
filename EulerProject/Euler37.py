def is_prime(num):
	val = True
	if num == 1:
		val = False
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

def check_right(num):
	temp = str(num)
	while len(temp) > 0:
		if is_prime(int(temp)):
			temp = temp[1:]
		else:
			return False
			break
	return True

def check_left(num):
	temp = str(num)
	while len(temp) > 0:
		if is_prime(int(temp)):
			temp = temp[:-1]
		else:
			return False
			break
	return True

summation = 0
for x in range(10,1000000):
	if check_right(x) and check_left(x):
		print x
		summation += x
print summation




		
		