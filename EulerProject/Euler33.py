prod = 1
for y in range(11,100):
	for x in range(11,y):
		str_num = str(x)
		str_den = str(y)
		if str_num[1] == str_den[0]: 
			if float(str_den[1]) != 0:
				red = float(str_num[0])/float(str_den[1])
				if red == float(x)/float(y) and x!=y and float(str_num[1]) != 0:
					print str_num, "and" , str_den
					prod *= red
		elif str_num[0] == str_den[1]:
			if float(str_den[0]) != 0:
				red = float(str_num[1])/float(str_den[0])
				if red == float(x)/float(y) and x!=y and float(str_num[1]) != 0:
					print str_num, "and" , str_den
					prod *= red
print prod

