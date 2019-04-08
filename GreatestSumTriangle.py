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


def brute_force(grid, i, j, k, l):
  if (i == len(grid)):
    l.append(k)

  else:
    k += grid[i][j]
    brute_force(grid, j, i + 1, l, k)
    brute_force(grid, j + 1, i + 1, l, k)

  return l


# returns the greatest path sum using greedy approach


def greedy(grid):
  totalSum, tempSum = 0, 0

  for i in range(len(grid)):
    if (len(grid[i]) >= 2):
      if grid[i][tempSum] > grid[i][tempSum + 1]:
        totalSum += grid[i][tempSum]
      else:
        totalSum += grid[i][tempSum + 1]
        totalSum += 1

    totalSum += grid[i][0]

  return totalSum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
  return

# returns the greatest path sum and the new grid using dynamic programming


def dynamic_prog(grid):
  for col in range(len(grid) - 2, -1, -1):
    for row range(col + 1):
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

  # output greatest path from exhaustive search
  times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming
  times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
  times = times / 10
  # print time taken using dynamic programming


if __name__ == "__main__":
  main()
