def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

# Create prime list
pl = []
for x in range(2,100000):
	if is_prime(x):
		pl.append(x)

# Initialize variables
summation = 0
sum_list = []

# Create summation lists
for y in pl:
	if summation < 1000000:
		sum_list.append(summation)
		summation += y
	else:
		break	
print sum_list

# Since the first number is not necessarily at index 1, find the differences of the sums
diffs = []
inddiff = []
for indz, z in enumerate(sum_list): 
	for inda, a in enumerate(sum_list):
		if z > a:
			if is_prime(z-a):
				diffs.append(z-a)
				inddiff.append(indz-inda)

# Find the index of the highest number in inddiff (meaning the most primes)
print max(inddiff)
# Find the corresponding summation at this point
print diffs[inddiff.index(max(inddiff))]


	