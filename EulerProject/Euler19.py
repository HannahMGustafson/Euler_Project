daynum = []
for y in range(1901,2001):
	for m in range(1,13):
		if m in [1,3,5,7,8,10,12]:
			for x in range(1,32):
				daynum.append(x)
		if m in [4, 6, 9, 11]:
			for x in range(1,31):
				daynum.append(x)
		if m is 2 and y%4 == 0:
			for x in range(1,30):
				daynum.append(x)
		if m is 2 and y%4 != 0:
			for x in range(1,29):
				daynum.append(x)
DOTW = 2 # Tu = 2, W = 3, Th = 4, F = 5, Sa = 6, Su = 7, M = 1
sun_on_first = 0
for day in daynum:
	if DOTW == 7 and day == 1:
		sun_on_first += 1
	DOTW += 1
	if DOTW == 8:
		DOTW -= 7

print sun_on_first
