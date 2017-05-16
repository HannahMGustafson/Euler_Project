file = open("text.txt", 'r')
nums = str(file.read())
nums = nums.replace('\n', '')

def prod(vals):
	p = 1
	for x in vals:
		p *= int(x)
	return p

maxval = 0
for n in range(0,1001-13):
	temp = prod(list(nums[n:n+13]))
	if temp>maxval:
		maxval = temp
print maxval