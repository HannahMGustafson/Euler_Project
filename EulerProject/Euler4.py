
def ispalindrome(num):
	forward = str(num)
	rev = forward[::-1]
	if forward == rev:
		return True
	else:
		return False



palis = []
for i in range(1000,800, -1):
 	for j in range(1000,800, -1):
 		mult = i * j
 		if ispalindrome(mult):
 			palis.append(mult)
print max(palis)
 