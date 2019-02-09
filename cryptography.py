
# function to encrypt string
def encrypt(strng):

    # makes empty matrix based on the length of the string
    if len(strng) <= 4:
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

    # iterates through the matrix and fills it with strng letters and *
    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if k < len(strng):
                matrix[i][j] = strng[k]
                k += 1
            else:
                matrix[i][j] = '*'

    # transposes matrix for encryption
    finalMatrix = list(zip(*matrix))

    # starts off with empty string and reads matrrix items and builds string
    encryptStr = ''
    for row in finalMatrix:
        rowStr = ''
        for item in row:
            if item != '*':
                rowStr += item
        encryptStr += rowStr[::-1]

    # returns encrypted word
    return(encryptStr)


def decrypt(strng):

    if len(strng) <= 4:
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
                k += 1
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


def main():

    print('Encryption:')
    fileEncrypt = open('encrypt-2.txt', 'r')
    n = int((fileEncrypt.readline()))

    for line in fileEncrypt:
        if len(str(line.strip())) < 2:
            print(str(line.strip()))
        else:
            print(encrypt(str(line.strip())))

    # print('Decryption:')
    # fileDecrypt = open('decrypt.txt', 'r')
    # n = int((fileDecrypt.readline()))

    # for line in fileDecrypt:
    #     if len(str(line.strip())) < 2:
    #         print(str(line.strip()))
    #     else:
    #         print(decrypt(str(line.strip())))


main()
