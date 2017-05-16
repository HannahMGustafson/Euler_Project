import string
def namescore(name):
	val = []
	let = list(string.ascii_uppercase)
	name = name[1:len(name)-1] #strip parentheses 
	for x in name:
		val.append(let.index(x)+1)
	return sum(val)


file = open('Euler22_text.txt', 'r')
temp = file.read()
word = list(temp.split(","))
word = sorted(word)
summation = 0
for idx, name in enumerate(word):
	summation += namescore(name)*(idx+1)
print summation









