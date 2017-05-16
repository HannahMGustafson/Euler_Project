import itertools

summation = 0
pd = '0123456789'
temp = itertools.permutations(pd)
vals = [int(''.join(x)) for x in temp]
for y in vals:
	t = str(y)
	if int(t[1:4])%2 == 0 and int(t[2:5])%3 == 0 and int(t[3:6])%5 == 0 and int(t[4:7])%7 == 0 and int(t[5:8])%11 == 0 and int(t[6:9])%13 == 0 and int(t[7:10])%17 == 0:
		print y
		summation += int(y)
print summation