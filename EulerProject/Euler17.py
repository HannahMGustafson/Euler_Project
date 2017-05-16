# sum 1 to 99
numct = 0
ones = [3, 3, 5, 4, 4, 3, 5, 5, 4] # 1-9
print sum(ones)
weirdos = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # 10-19
tens = [6, 6, 5, 5, 5, 7, 6, 6] # 20-90
numct = 10*(sum(weirdos) + sum(tens)*10 + sum(ones)*9)
andct = 3*99*9
hundct = sum(ones)*100+7*9*100
thousct = len('onethousand')
numct = numct+andct+hundct+thousct
print numct