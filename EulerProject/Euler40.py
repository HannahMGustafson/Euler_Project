nums = []
dig = 0
for x in range(1,1000000):
	if dig < 1000001:
		nums += str(x)
		dig += len(str(x))
print int(nums[14])
print int(nums[0])*int(nums[9])*int(nums[99])*int(nums[999])*int(nums[9999])*int(nums[99999])*int(nums[999999])