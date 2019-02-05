import math

#  File: Intervals.py

#  Description: Algorithm finds overalapping intervals and makes them into one. The tuples are then sorted by size/

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/3/2019

#  Date Last Modified: 2/4/2019

# function that opens the textfile and makes list of tuples
def fileOpen():
  list1 = []

  intFile = open('intervals5.txt', 'r')
  for line in intFile:
    if line != '':
      line.strip('\n')
      num1 = int(line.split(' ')[0])
      num2 = int(line.split(' ')[1])
      tup = (num1, num2)
      list1.append(tup)

  return list1

# function makes the overalapping intervals
def intervals(fileOpen):

  # sorting the tuple list
  fileOpen = sorted(fileOpen, reverse=False)
  finalList = []

  # setting variables to be used in algorithm
  first = fileOpen[0]
  start = first[0]
  end = first[1]

  # for loop iterates from the 2nd term onward and compares [0] and [1] indices of neighboring tuples
  for interval in fileOpen[1:]:
    if end >= interval[0]:

      # finds max of neighboring tuples
      end = max(end, interval[1])

    else:

      # updates overlapping tuple to include the neighboring values
      finalList.append(tuple([start, end]))
      start = interval[0]
      end = interval[1]

  # appends tuple if doesn't overalap with the previous tuple
  finalList.append(tuple([start, end]))

  # prints tuples in line
  for interval in finalList:
    print(interval)


def main():
  file = fileOpen()
  intervals(file)


main()
