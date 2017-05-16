file = open("Euler67_text.txt", "r")
output = []
lines = 100
for x in range(0,lines):
	temp = file.readline()
	temp = temp.replace('\n', '')
	temp = temp.split(' ')
	output.insert(0,temp)


for r in range(1,lines):
	temprow = []
	for c in range(0,len(output[r])):
		temp1 = int(output[r][c]) + int(output[r-1][c])
		temp2 = int(output[r][c]) + int(output[r-1][c+1])
		temprow.append(max(temp1, temp2))
	output[r] = temprow
	print output






