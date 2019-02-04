#  File: Spiral.py

#  Description: Algorithm that finds sum of surrounding numbers of a given int

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 1/31/2019

#  Date Last Modified: 2/1/2019



# spiral function that makes spiral with one paramter 'n'
def spiral(n):

    n = n + 2
    matrix = [[0] * (n) for i in range(n)]

    # setting variables up
    rowStart = 1
    rowEnd = n - 2
    colStart = 1
    colEnd = n - 2

    beginNum = (n - 2) * (n - 2)

    # while loop to make sure conditions are met so it can continue
    while (rowStart <= rowEnd and colStart <= colEnd):

        # goes and makes one column on one side of square
        for col in range(colStart, colEnd + 1):
            matrix[rowStart][col] = beginNum
            beginNum -= 1

        rowStart += 1

        # goes and makes one column on one side of square
        for row in range(rowStart, rowEnd + 1):
            matrix[row][colEnd] = beginNum
            beginNum -= 1

        colEnd -= 1

        # goes and makes one column on one side of square
        for col in range(colEnd, colStart - 1, -1):
            matrix[rowEnd][col] = beginNum
            beginNum -= 1

        rowEnd -= 1

        # goes and makes one column on one side of square
        for row in range(rowEnd, rowStart - 1, -1):
            matrix[row][colStart] = beginNum
            beginNum -= 1

        colStart += 1

    return(matrix)

# sums all values around n
def sumNum(matrix, n):

    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == n:
                count += matrix[i][j + 1]
                count += matrix[i][j - 1]
                count += matrix[i - 1][j]
                count += matrix[i - 1][j - 1]
                count += matrix[i - 1][j + 1]
                count += matrix[i + 1][j]
                count += matrix[i + 1][j + 1]
                count += matrix[i + 1][j - 1]

    return(count)



# main calls the function and reads the text file
def main():
    
    # opening text file to be read
    inSpiral = open('spiral.txt', 'r')
    n = int((inSpiral.readline()))

    matrix = spiral(n)

    # printing sum of surrounding nums
    for line in inSpiral:
        print(sumNum(matrix, int(line)))


main()
