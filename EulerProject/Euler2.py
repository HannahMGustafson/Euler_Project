fib = [1,2]
summation = 2
ind = 2
while fib[-1] < 4000000:
	fib.append(fib[ind-1] + fib[ind-2])
	if fib[ind]%2 == 0:
		summation += fib[ind]
	ind += 1
print summation