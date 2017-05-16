def check_pd(all_nums):

	if str(0) in all_nums:
		return False
	for n in range(1,10):
		if all_nums.count(str(n)) != 1:
			return False
	return True 


for x in range(1,100000):
	all_nums = []
	y = 1
	while len(all_nums) <= 8:
		all_nums += str(x*y)
		y += 1
	if len(all_nums) == 9:
		if check_pd(all_nums):
			print all_nums
