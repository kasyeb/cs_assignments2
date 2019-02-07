
#ENCRYPT
# crypt1 = [['g','o','n','e'],
# 		  ['w','i','t','h'],
# 		  ['t','h','e','w'],
# 		  ['i','n','d','*']]

crypt1 = [['t','h','e','c'],
		  ['o','n','t','e'],
		  ['s','t','i','s'],
		  ['o','v','e','r']]
for row in crypt1:
	print(row)
print('---------')
crypt1_t = list(zip(*crypt1))
for row in crypt1_t:
	print(row)

emptyStr = ''
for row in crypt1_t:
	rowStr = ''
	for item in row:
		if item != '*':
			rowStr += item
	emptyStr += rowStr[::-1]
print(emptyStr)

# for i in range(len(crypt1_t)-1,-1):
# 	for j in range(len(crypt1_t)-1,-1):

#
