#  File: Work.py 

#  Description:Finds the most effective way for Vyasa to study and write lines of code

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/4/2019

#  Date Last Modified:

# binary search which finds v by calling linesCode function
def binSearch(n, k):
  low = 1
  high = n

# simple structure like binary code
  while (low <= high):
    middle = (low + high) // 2
    if linesCode(n, k, middle) == False:
      low = middle + 1

    else:
      if linesCode(n, k, middle) == True:
        high = middle - 1
        v = middle

  return v 

# goes through values while 2 conditions are not met
def linesCode(n, k, middle):
  start = 1
  count = middle

  while ((count < n) and (middle // k ** start != 0)):
    count += (middle // (k ** start))
    start += 1

# result here is returned back to the binSearch function
  if count >= n:
    return True

  else:
    return False

# main parses text file and assigns n and k to binsearch
def main():
  file = open('work.txt', 'r')
  numTestCases = int(file.readline())

  for i in range(numTestCases):
    line = file.readline()
    line1 = line.split(' ')
    n = int(line1[0])
    k = int(line1[1])

    print(binSearch(n, k))

main()
