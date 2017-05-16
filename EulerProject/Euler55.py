def palindrome(num):
	temp = str(num)
	new_num = ""
	for x in temp[::-1]:
		new_num += x
	return int(new_num)

def is_palindrome(num):
	if num == palindrome(num):
		return True
	else:
		return False

Lychrel = 0
for y in range(1,10001):
	ct = 0
	while ct < 50:
		y = y + palindrome(y)
		if is_palindrome(y):
			break
		ct += 1
		if ct == 50:
			Lychrel += 1
print Lychrel

