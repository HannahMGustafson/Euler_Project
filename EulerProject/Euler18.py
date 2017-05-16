file = open("Euler18_text.txt", "r")
output = []
for x in range(0,15):
	temp = file.readline()
	temp = temp.replace('\n', '')
	temp = temp.split(' ')
	output.insert(0,temp)
print output[0][1]

for r in range(1,15):
	temprow = []
	print len(output[r])
	for c in range(0,len(output[r])):
		temp1 = int(output[r][c]) + int(output[r-1][c])
		temp2 = int(output[r][c]) + int(output[r-1][c+1])
		temprow.append(max(temp1, temp2))
	output[r] = temprow
	print output






