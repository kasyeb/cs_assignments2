#  File: Boxes.py

#  Description: Algorithm sees if boxes can be inside each other

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/20/2019

#  Date Last Modified: 3/25/2019

# checks if boxes fit
def fit(box1, box2):
  if ((box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])):
    return True

  else:
    return False

# helper function
def helper(val):
  for i in range(0, len(val) - 1):
    if fit(val[i], val[i + 1]) == True:
      return False
    else:
      return True

# helper function and subset algorithm nested together
def subsets(i, j, k, l):
  fitted = True

  if (l == len(i)):
    for nums in range(len(j) - 1):
      if fit(j[nums], j[nums + 1]) == False:
        fitted = False

    if fitted == True:
      k.append(j)

  # subset algorithm
  else:
    new = j[:]
    j.append(i[l])
    subsets(i, new, k, l + 1)
    subsets(i, j, k, l + 1)


def main():
  # open file for reading
  in_file = open("./boxes.txt", "r")

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create an empty list of boxes
  boxList = []
  subsetList = []
  nestedBoxesList = []
  tempBoxList = []

  # read the list of boxes from the file
  for i in range(num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range(len(box)):
      box[j] = int(box[j])
    box.sort()
    boxList.append(box)

  boxList.sort()
  in_file.close()

  subsets(boxList, nestedBoxesList, subsetList, 0)

  val = 2
  for i in subsetList:
    if len(i) > val:
      val = len(i)

  # finds the biggest box size
  maxBox = []
  for i in subsetList:
    if len(i) == val:
      maxBox.append(i)

  # prints values
  if len(maxBox) != 0:
    print('Largest Subset of Nesting Boxes')
    maxBox.sort()
    for i in maxBox:
      for j in range(len(i)):
        print(i[j])
      print()

  else:
    print('No Nesting Boxes')


main()
