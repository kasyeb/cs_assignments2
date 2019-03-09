# File: Pancake.py

# Description: Sorting by flips only

# Student's Name: Vinayak Sahal

# Student's UT EID: vs9736

# Course Name: CS 313E

# Unique Number: 50725

# Date Created: 3/8/2019

# Date Last Modified: 3/8/2019

# function to sort array
def pancake(arr):
  flipped = False
  orderedArr = sorted(arr)

# checks to see if its already sorted
  if arr == orderedArr:
    print(0)
  else:
    print(1, end = ' ')
    print(0)

  count = 0
  i = len(arr)

  while flipped:
    # finds index of mac
    maxInt = arr.index(max(arr[0:i]))
    # string splicing to make new array
    # arr = arr[maxInt::-1] + arr[maxInt + 1:len]
    if arr == orderedArr:
      break
    else:
      count += 1
      print(count, end = ' ')

# calling main function
def main():
  file = open('pancake.txt', 'r')
  for line in file:
    line1 = line.strip('\n')
    line1 = line1.split(' ')
    for i in line1:
      print(i, end=' ')
    print()
    pancake(line1)

main()

