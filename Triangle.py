#  File: Triangle.py

#  Description: Finds maximum sum of triangle

#  Student's Name: Vinayak Sahal

#  Student's UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/7/2019

#  Date Last Modified: 4/8/2019


from timeit import timeit

# returns the greatest path sum using exhaustive search


def brute_force(grid):
  m = []
  bruteForceHelper(grid, 0, 0, 0, m)

  return m

# helper function that uses recursion


def bruteForceHelper(i, j, k, l, m):
  if (j == len(i)):
    m.append(l)

  else:
    l += int(i[j][k])
    return bruteForceHelper(i, j + 1, k, l, m) or bruteForceHelper(i, j + 1, k + 1, l, m)

# returns the greatest path sum using greedy approach


def greedy(grid):
  totalSum, tempSum = 0, 0

  # finds the max value in the adjacent rows and sums them
  for i in range(len(grid)):
    if (len(grid[i]) >= 2):
      if int(grid[i][tempSum]) > int(grid[i][tempSum + 1]):
        totalSum += int(grid[i][tempSum])
      else:
        totalSum += int(grid[i][tempSum + 1])
        tempSum += 1

    else:
      totalSum += int(grid[i][0])

  return totalSum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
  divideConquerHelper(grid, 0, 0)


# recursive helper function to divide and conquer
def divideConquerHelper(grid, i, j):
  if i >= len(grid):
    return 0

  else:
    m = divideConquerHelper(grid, i + 1, j)
    n = divideConquerHelper(grid, i + 1, j + 1)

    count = max(m, n) + int(grid[i][j])

  return count

# returns the greatest path sum and the new grid using dynamic programming
# finds max of each row and adds values


def dynamic_prog(grid):
  # bottom up
  for col in range(len(grid) - 2, -1, -1):
    for row in range(col + 1):
      grid[col][row] = int(grid[col][row]) + max(int(grid[col + 1][row]), int(grid[col + 1][row + 1]))

  return (grid[0][0])


# reads the file and returns a 2-D list that represents the triangle
def read_file():
  triangle = []

  file = open('triangle.txt', 'r')

  numLines = file.readline()
  numLines = int(numLines.strip())

  for i in range(numLines):
    triRow = file.readline()
    triRow = triRow.strip()
    triRow = triRow.split()
    triangle.append(triRow)

  return triangle


def main():
  # read triangular grid from file
  grid = read_file()

  totalSums = brute_force(grid)
  bruteForceAnswer = max(totalSums)

  # output greatest path from exhaustive search
  times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
  times = times / 10
  # print time taken using exhaustive search
  print('The greatest path sum through exhaustive search is ' + str(bruteForceAnswer) + '.')
  print('The time taken for exhaustive search is ' + str(times) + ' seconds.')
  print()

  # output greatest path from greedy approach
  times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
  times = times / 10
  greedyAnswer = greedy(grid)

  # print time taken using greedy approach
  print('The greatest path sum through greedy search is ' + str(greedyAnswer) + '.')
  print('The time taken for greedy approach is ' + str(times) + ' seconds.')
  print()

  # output greatest path from divide-and-conquer approach
  times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
  times = times / 10
  divideAndConquerAnswer = divide_conquer(grid)
  # print time taken using divide-and-conquer approach
  print('The greatest path sum through recursive search is ' + str(divideAndConquerAnswer) + '.')
  print('The time taken for recursive search is ' + str(times) + ' seconds.')
  print()

  # output greatest path from dynamic programming
  times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
  times = times / 10
  dynamicProgrammingAnswer = dynamic_prog(grid)
  # print time taken using dynamic programming
  print('The greatest path sum through dynamic programming is ' + str(dynamicProgrammingAnswer) + '.')
  print('The time taken for dynamic programming is ' + str(times) + ' seconds.')
  print()


if __name__ == "__main__":
  main()
