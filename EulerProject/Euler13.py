
digsum = 0
carryover = 0
revnum = []
for d in range (49,-1, -1):
	file = open ("Euler13_text.txt", "r")
	for r in range(1,101):
		temp = str(file.readline())
		digsum += int(temp[d])
	if d == 0:
		firstdigs = (digsum)
		print firstdigs
		print revnum
	else:
		carryover = int(digsum/10)
		remainder = digsum-carryover*10
		revnum.append(remainder)
		digsum = carryover

		




