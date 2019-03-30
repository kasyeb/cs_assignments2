#  File: MagicSquare.py

#  Description: Finds magic squares

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/27/2019

#  Date Last Modified: 3/29/2019

# makes matrix


def matrixMaker(val):
  matrix = [[val[0], val[1], val[2], val[3]]
            [val[4], val[5], val[6], val[7]]
            [val[8], val[9], val[10], val[11]]
            [val[12], val[13], val[14], val[15]]]

  return matrix

# permutes through options


def square(i, j, k):
  index = 0
  if (k == index):
    pass
  else:
    if (j == len(i)):
      if (i[12] + i[13] + i[14] + i[15]) != 34:
        return
      else:
        # checks if its magic square
        if isMagicSquare(i) == True:
          printMagicSquare(matrixMaker(i))
    else:
      if (j == 4):
        if (i[0] + i[1] + i[2] + i[3]) != 34:
          return
        else:
          # finds all the permutations
          for values in range(j, len(i)):
            newSet = i[:]
            newSet[j], newSet[values] = newSet[values], newSet[j]
            square(newSet, j + 1, k)
            newSet[j], newSet[values] = newSet[values], newSet[j]

      elif(j == 8):
        if (i[4] + i[5] + i[6] + i[7]) != 34:
          return
        else:
          for values in range(j, len(i)):
            newSet = i[:]
            newSet[j], newSet[values] = newSet[values], newSet[j]
            square(newSet, j + 1, k)
            newSet[j], newSet[values] = newSet[values], newSet[j]

      elif(j == 12):
        if (i[8] + i[9] + i[10] + i[11]) != 34:
          return
        else:
          for values in range(j, len(i)):
            newSet = i[:]
            newSet[j], newSet[values] = newSet[values], newSet[j]
            square(newSet, j + 1, k)
            newSet[j], newSet[values] = newSet[values], newSet[j]

# checks if values add up to the sum (34)


def isMagicSquare(val):
  if ((val[0] + val[1] + val[2] + val[3] == 34) and
      (val[4] + val[5] + val[6] + val[7] == 34) and
      (val[8] + val[9] + val[10] + val[11] == 34) and
      (val[12] + val[13] + val[14] + val[15] == 34) and
      (val[0] + val[5] + val[10] + val[15] == 34) and
          (val[3] + val[6] + val[9] + val[12] == 34)):
    return True
  else:
    return False

# need to format square (output)


def printMagicSquare(nums):
  for i in nums:
    print(i)


def main():
  cases = int(input('Enter number of magic squares (1-20): '))
  print()
  nums = []
  for i in range(16):
    nums.append(int(i + 1))
  square(nums, 0, cases)


main()
