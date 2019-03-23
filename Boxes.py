def f1():
  pass

def f2():
  pass

def main():
  # open file for reading
  in_file = open ("./boxes.txt", "r")

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list of boxes
  box_list = []

  # read the list of boxes from the file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  print (box_list)
  print()

  # sort the box list
  box_list.sort()
  print (box_list)
  print ()

  # get all subsets of boxes

  # check if all the boxes in a given subset fit
  # keep track of it

  # print all the largest subset of boxes


main()
