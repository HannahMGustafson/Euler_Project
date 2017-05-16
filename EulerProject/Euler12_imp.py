
def primes_below(num):
	primes = []
	for y in range(2,num+1):
		is_prime = True
		for x in range(2,y-1):
			if y%x == 0:
				is_prime = False
		if is_prime == True:
			primes.append(y)
	return primes

primes = primes_below(15000)
print primes

def is_prime_check(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

def find_factors(tri):
	final = tri
	exp = 1
	#check prime
	check_ans = is_prime_check(final)
	if check_ans == False:
		while final != 1:
			for x in primes:
				texp = 1
				while final%x == 0:
					final = final/x
					texp += 1
				exp *= texp
			if final in primes:
				break
	print exp
	return exp

divisors = 0
n = 0
while divisors < 500:
	n += 1
	tritemp = (n*(n+1))/2
	divisors = find_factors(tritemp)
print tritemp


