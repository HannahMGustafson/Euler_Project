def ispalindrome(num):
	forward = str(num)
	rev = forward[::-1]
	if forward == rev:
		return True
	else:
		return False

summation = 0
for x in range(1,1000001):
	if ispalindrome(x):
		temp = bin(x)
		val = int(temp[2:])
		if ispalindrome(val):
			summation += x
			print x
print summation