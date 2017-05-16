import math

count = 0
for n in range(1,101):
	for r in range(1,101):
		if r <= n:
			temp = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
			if temp > 1000000:
				count += 1
print count