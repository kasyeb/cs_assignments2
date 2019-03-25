#  File: Boxes.py

#  Description: Algorithm sees if boxes can be inside each other

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/20/2019

#  Date Last Modified: 3/21/2019


def fit(box1, box2):
  if ((box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])):
    return True
  else:
    return False


def subsets(i, j, k, l):
  condition = True
  if l == len(i):
    for nums in range(len(j) - 1):
      if fit(j[nums], j[nums + 1]) == False:
        condition = False

    if condition == True:
      k.append(j)

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
  box_list = []

  # read the list of boxes from the file
  for i in range(num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range(len(box)):
      box[j] = int(box[j])
    box.sort()
    box_list.append(box)

  # close the file
  in_file.close()

  print(box_list)
  print()

  # sort the box list
  box_list.sort()
  print(box_list)
  print()

  # get all subsets of boxes

  # check if all the boxes in a given subset fit
  # keep track of it

  # print all the largest subset of boxes
  # look at mitra notes


main()
