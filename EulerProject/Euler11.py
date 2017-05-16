file = open('Euler11_text.txt', 'r')
lol = []
currmax = 0
for x in range(0,20):
	nums = file.readline()
	nums = nums.replace('\n', '')
	nums = nums.split(' ')
	lol.append(nums)
print lol[0][3] #row, column

#left/right
for r in range(0,20):
	for c in range(0,16):
		temp = int(lol[r][c])*int(lol[r][c+1])*int(lol[r][c+2])*int(lol[r][c+3])
		if temp > currmax:
			currmax = temp

#up/down
for r in range(0,16):
	for c in range(0,20):
		temp = int(lol[r][c])*int(lol[r+1][c])*int(lol[r+2][c])*int(lol[r+3][c])
		if temp > currmax:
			currmax = temp

#diags going down
for r in range(0,16):
	for c in range(0,16):
		temp = int(lol[r][c])*int(lol[r+1][c+1])*int(lol[r+2][c+2])*int(lol[r+3][c+3])
		if temp > currmax:
			currmax = temp

#diags going up
for r in range(0,16):
	for c in range(3,20):
		temp = int(lol[r][c])*int(lol[r+1][c-1])*int(lol[r+2][c-2])*int(lol[r+3][c-3])
		if temp > currmax:
			currmax = temp
print currmax