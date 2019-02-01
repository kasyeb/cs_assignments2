#  File: Spiral.py

#  Description:

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 1/31/2019

#  Date Last Modified: 2/1/2019


def spiral():

  spiralFile = open('spiral.txt', 'r')
  n = int((spiralFile.readline()))
  n = n + 2

  matrix = [[0] * (n) for i in range(n)]

  rowStart = 1
  rowEnd = n - 2
  colStart = 1
  colEnd = n - 2

  beginNum = (n - 2) * (n - 2)

  while (rowStart <= rowEnd and colStart <= colEnd):

    for col in range(colStart, colEnd + 1):
      matrix[rowStart][col] = beginNum
      beginNum -= 1

    rowStart += 1

    for row in range(rowStart, rowEnd + 1):
      matrix[row][colEnd] = beginNum
      beginNum -= 1

    colEnd -= 1

    for col in range(colEnd, colStart - 1, -1):
      matrix[rowEnd][col] = beginNum
      beginNum -= 1

    rowEnd -= 1

    for row in range(rowEnd, rowStart - 1, -1):
      matrix[row][colStart] = beginNum
      beginNum -= 1

    colStart += 1

  return matrix


matrix = spiral()

for row in matrix:
  print(row)


count = 0

for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == :
      count += matrix[i][j + 1]
      count += matrix[i][j - 1]
      count += matrix[i - 1][j]
      count += matrix[i - 1][j - 1]
      count += matrix[i - 1][j + 1]
      count += matrix[i + 1][j]
      count += matrix[i + 1][j + 1]
      count += matrix[i + 1][j - 1]

print(count)
