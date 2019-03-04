#  File: Work.py 

#  Description:Finds the most effective way for Vyasa to study and write lines of code

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/4/2019

#  Date Last Modified: 2/4/2019


def binSearch(n, k):
  low = 1
  high = n

  while (low <= high):
    middle = (low + high) // 2
    if linesCode(n, k, middle) == False:
      low = middle + 1

    else:
      if linesCode(n, k, middle) == True:
        high = middle - 1
        v = middle

  return v 


def linesCode(n, k, middle):
  start = 1
  count = middle

  while ((count < n) and (middle // k ** start != 0)):
    count += (middle // (k ** start))
    start += 1

  if count >= n:
    return True

  else:
    return False


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
