import itertools
vals = []
for x in itertools.permutations('0123456789'):
	temp = ''.join(x)
	vals.append(temp)
temp2 = sorted(vals)
print len(temp2)
print temp2[999999]