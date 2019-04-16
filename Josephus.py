#  File: Josephus.py

#  Description: Circular linked list assignment for soliders

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/15/2019

#  Date Last Modified:

# Link class
class Link(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

# circular list class
class CircularList(object):
  # Constructor
  def __init__(self):
    self.first = None

    # Insert an element (value) in the list
    # similar to prev assignment?
  def insert(self, data):
    # making new linked list with data
    # count how many items are added?
    counter = 0
    new_link = Link(data, self.first)
    current = self.first

    # checks to see if current isnt null
    if (current == None):
      self.first = new_link
      self.first.next = self.first
      return
    
    # when location reached insert data
    while (current.next != self.first):
      current = current.next
      counter += 1

    current.next = new_link
    new_link.next = self.first

    # Find the link with the given data (value)
    #smilar to prev assignment
  def find(self, data):
    current = self.first
    
    while(current.data != data):
      current = current.next

    return current

    # Delete a link with a given data (value)
  def delete(self, data):
    #make double copy of data
    current, previous = self.first, self.first

    while (current.data != data):
      previous = current
      current = current.next

    if (current != self.first):
      previous.next = current.next

    else:
    # check to see if last link, if it is link it to first one
      self.isLast()
      self.first = self.first.next

    return current.data

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
  def delete_after(self, start, n):
    current = self.find(start)

    for i in range(n - 1):
      current = current.next

      # print statement?

    dataDelete = self.delete(current.data)

    return (dataDelete, current.next.data)

    # Return a string representation of a Circular List
  def __str__(self):
    current = self.first
    soilderStr = ''
    
    #do loop of entire list to copy down numbers
    while (current.next != self.first):
      soilderStr += str(current.data) 

      # go to next data
      current = current.next

    return soilderStr

# check to see if link is last (link first and last)
  def isLast(self):
    current = self.first

    while(current.next != self.first):
      current = current.next

    current.next = self.first.next

#should implement length function to see if list is equal to text file?

def main():
  in_file = open('josephus.txt', 'r')

  totalSoilders = int(in_file.readline())
  start = int(in_file.readline())
  increment = int(in_file.readline())

  soilderCircularList = CircularList()

  # adds all soilders to a list till totalSoilders
  for i in range(totalSoilders):
    soilderCircularList.insert(i + 1)

  # deletes it one by one
  soilderStr = ''
  for j in range(totalSoilders):
    out, start = soilderCircularList.delete_after(start, increment)
    soilderStr += (str(out) + '\n') # new line format

  print(soilderStr)


main()
