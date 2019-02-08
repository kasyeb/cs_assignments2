

def encrypt(strng):

    if len(strng) == 1:
        return str
    elif len(strng) <= 4:
        matrix = [[None] * 2 for i in range(2)]

    elif len(strng) <= 9:
        matrix = [[None] * 3 for i in range(3)]

    elif len(strng) <= 16:
        matrix = [[None] * 4 for i in range(4)]

    elif len(strng) <= 25:
        matrix = [[None] * 5 for i in range(5)]

    elif len(strng) <= 36:
        matrix = [[None] * 6 for i in range(6)]

    elif len(strng) <= 49:
        matrix = [[None] * 7 for i in range(7)]

    elif len(strng) <= 64:
        matrix = [[None] * 8 for i in range(8)]

    elif len(strng) <= 81:
        matrix = [[None] * 9 for i in range(9)]

    elif len(strng) <= 100:
        matrix = [[None] * 10 for i in range(10)]

    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if k < len(strng):
                matrix[i][j] = strng[k]
                k += 1
            else:
                matrix[i][j] = '*'

    finalMatrix = list(zip(*matrix))

    encryptStr = ''
    for row in finalMatrix:
        rowStr = ''
        for item in row:
            if item != '*':
                rowStr += item
        encryptStr += rowStr[::-1]

    print(encryptStr)


encrypt('thecontestisover')

def decrypt(strng):

    if len(strng) == 1:
        return str
    elif len(strng) <= 4:
        matrix = [[None] * 2 for i in range(2)]

    elif len(strng) <= 9:
        matrix = [[None] * 3 for i in range(3)]

    elif len(strng) <= 16:
        matrix = [[None] * 4 for i in range(4)]

    elif len(strng) <= 25:
        matrix = [[None] * 5 for i in range(5)]

    elif len(strng) <= 36:
        matrix = [[None] * 6 for i in range(6)]

    elif len(strng) <= 49:
        matrix = [[None] * 7 for i in range(7)]

    elif len(strng) <= 64:
        matrix = [[None] * 8 for i in range(8)]

    elif len(strng) <= 81:
        matrix = [[None] * 9 for i in range(9)]

    elif len(strng) <= 100:
        matrix = [[None] * 10 for i in range(10)]

    matrix1 = list(zip(*matrix))

    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if k < len(strng):
                matrix[i][j] = strng[k]
                k +=1
            else:
                matrix[i][j] = '*'

    finalMatrix = list(zip(*matrix))

    decryptStr = ''
    for row in finalMatrix:
        rowStr = ''
        for item in row:
            if item != '*':
                rowStr += item
        decryptStr += rowStr[::-1]

    print(decryptStr[::-1])

decrypt('itwgnhiodetnwhe')



# def decrypt(strng):
#   #If len(str) < 2: return strng?
#   pass

# def main():
#   fileEncrypt = open('encrypt.txt', 'r')
#   n = int((fileEncrypt.readline()))
#   for i in range(n):
#       print(encrypt())

#   fileDecrypt = open('decrypt.txt', 'r')
#   m = int((fileDecrypt.readline()))
#   for i in range(m):
#       print(decrypt())
