import itertools

def is_prime(num):
	val = True
	for x in range(2,int(num**0.5)+1):
		if num%x == 0:
			val = False
			break
	return val

for x in range(1000, 10000):
	vals = []
	diffs = []
	if is_prime(x):
		temp = list(itertools.permutations(str(x)))
		temp = [int(''.join(x)) for x in temp]
		for x in temp:
			if x > 1000 and x not in vals:
				if is_prime(x):
					vals.append(x)
		if len(vals)>=3:
			for y in vals:
				for z in vals:
					if y-z != 0 and y-z > 0:				
						diffs.append(y-z)
		for y in diffs:
			if diffs.count(3330) >= 1 and diffs.count(6660) >= 1:
				print vals

