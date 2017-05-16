
ct = 0
for n in range(2,1000):
	it = 1
	num = 1
	den = 2
	while it < n:
		num_new = den
		den_new = num + 2*den
		it += 1
		num = num_new
		den = den_new
	num_new = den_new + num_new
	if len(str(num_new)) != len(str(den_new)):
		ct += 1

print ct
	# print len(str(vals[0]))
	# print len(str(vals[1]))
	# if len(str(vals[0]))>
