import string
def trinum(num):
	out = (-1 + (1+8*num)**0.5)/2
	if out == int(out):
		return True
	else:
		return False

def triword(s):
	wordval = 0
	let = list(string.ascii_uppercase)
	s = s[1:-1]
	for x in s:
		wordval += let.index(x)+1
	if trinum(wordval):
		return 1
	else:
		return 0


summation = 0
file = open('Euler42_text.txt', 'r')
words = file.read()
temp = list(words.split(','))
for x in temp:
	summation += triword(x)
	print summation