fib = ['1', '1']
n = 2
while len(str(fib[n-1]))<1000:
	fib.append(str(int(fib[n-2])+int(fib[n-1])))
	n += 1
print n