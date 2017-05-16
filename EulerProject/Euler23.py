# find a list of all abundant sums up to 28123
maxval = 28124
def sum_factors(num):
	summation = 0
	for x in range(1,num/2 + 1):
		if num%x == 0:
			summation += x
	return summation

abund = []
for x in range(1,maxval):
	if sum_factors(x)>x:
		abund.append(x)
print len(abund)

# sum each number with each other number

sums = []
for a in abund:
	for b in abund:
		# if b<(maxval/2) and (a+b) not in sums:
		sums.append(a+b)
sums = set(sorted(i for i in sums if i< maxval))

allval = set(range(1,maxval))
print sum(allval^sums)



