#  File: Spiral.py

#  Description:

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 1/31/2019

#  Date Last Modified: 2/1/2019


# def spiral(n):

    spiralFile = open('spiral.txt', 'r')
    n = int((spiralFile.readline()))

#   matrix = [[0] * n for i in range(n)]

#   rowStart = 0
#   rowEnd = n - 1
#   colStart = 0
#   colEnd = n - 1

#   beginNum = n * n

#   while (rowStart <= rowEnd and colStart <= colEnd):

#     for col in range(colStart, colEnd + 1):
#       matrix[rowStart][col] = beginNum
#       beginNum -= 1

#     rowStart += 1

#     for row in range(rowStart, rowEnd + 1):
#       matrix[row][colEnd] = beginNum
#       beginNum -= 1

#     colEnd -= 1

#     for col in range(colEnd, colStart - 1, -1):
#       matrix[rowEnd][col] = beginNum
#       beginNum -= 1

#     rowEnd -= 1

#     for row in range(rowEnd, rowStart - 1, -1):
#       matrix[row][colStart] = beginNum
#       beginNum -= 1

#     colStart += 1

#   return matrix


# spiral2 = spiral(10)

# for row in spiral2:
#   print(row)

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15]]

count = 0

for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == 9:
      count += matrix[i][j + 1]
      count += matrix[i][j - 1]
      count += matrix[i - 1][j]
      count += matrix[i - 1][j - 1]
      count += matrix[i - 1][j + 1]
      count += matrix[i + 1][j]
      count += matrix[i + 1][j + 1]
      count += matrix[i + 1][j - 1]

print(count)
