def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

# Generate Goldbach list
gb =[]
for i in range(3,10000):
	if is_prime(i):
		for j in range(1,75):
			gb.append(i+2*j*j)
print max(gb)

# Check if composite numbers are in that list
for x in range(9,10000,2):
	if is_prime(x) is False:
		if x not in gb:
			print x
			break

