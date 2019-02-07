
#ENCRYPT
# crypt1 = [['g','o','n','e'],
# 	    ['w','i','t','h'],
# 	    ['t','h','e','w'],
# 	    ['i','n','d','*']]

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

#DECRYPT
decrypt1 = [['o','s','o','t'],
	    ['v','t','n','h'],
	    ['e','i','t','e'],
	    ['r','s','e','c']]

decrypt_1 = list(zip(*decrypt1))
for row in decrypt_1:
	print(row)

emptyStr = ''
for row in decrypt_1:
	rowStr = ''
	for item in row:
		if item != '*':
			rowStr += item
	emptyStr += rowStr[::-1]
print(emptyStr[::-1])

# Matrix maker
def matrixMaker(str):
  if len(str) == 1:
    return str
  if len(str) <= 4:
    matrix = [[None] * 2 for i in range(2)]
    return matrix
  if len(str) <= 9:
    matrix = [[None] * 3 for i in range(3)]
    return matrix
  if len(str) <= 16:
    matrix = [[None] * 4 for i in range(4)]
    return matrix
  if len(str) <= 25:
    matrix = [[None] * 5 for i in range(5)]
    return matrix
  if len(str) <= 36:
    matrix = [[None] * 6 for i in range(6)]
    return matrix
  if len(str) <= 49:
    matrix = [[None] * 7 for i in range(7)]
    return matrix
  if len(str) <= 64:
    matrix = [[None] * 8 for i in range(8)]
    return matrix
  if len(str) <= 81:
    matrix = [[None] * 9 for i in range(9)]
    return matrix
  if len(str) <= 100:
    matrix = [[None] * 10 for i in range(10)]
    return matrix

# populating made matrix with letters from words
matrix2 = [[None] * 4 for i in range(4)]

word = 'thecontestisover'
word1 = 'gonewiththewind'

k = 0
for i in range(len(matrix2)):
	for j in range(len(matrix2)):
		matrix2[i][j] = word[k] # works for words with length of a square number, else I get index error
		k +=1 

print(matrix2)


