max_dig_sum = 0
for a in range(1,101):
	for b in range(1,101):
		temp = sum(int(digit) for digit in str(a**b))
		if temp > max_dig_sum:
			max_dig_sum = temp
print max_dig_sum