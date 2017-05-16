import itertools
import math
for gridsize in range(1,4):
	moves = []
	for x in range(0,gridsize):
		moves.append(1)
		moves.append(2)
	print moves
	print len(list(set(itertools.permutations(moves))))

ans = math.factorial(40)/(math.factorial(20)*math.factorial(20))
print ans







