#  File: Josephus.py

#  Description: Circular linked list assignment for soliders

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/15/2019

#  Date Last Modified:


class Link(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class CircularList(object):
  # Constructor
  def __init__(self):
    self.first = None

    # Insert an element (value) in the list
  def insert(self, data):
    new_link = Link(data)
    current = self.first

    if (current == None):
      self.first = new_link
      new_link.next = new_link
      return

    while (current.next != self.first):
      current = current.next

    current.next = new_link
    new_link.next = self.first

    # Find the link with the given data (value)
  def find(self, data):
    current = self.first

    while(current.data != data):
      current = current.next

    return current

    # Delete a link with a given data (value)
  def delete(self, data):
    current = self.first
    previous = self.first

    while(previous.next != self.first):
      previous = previous.next

    while (current.data != data):
      previous = current
      current = current.next

    if (self.first != self.first.next):
      self.first = current.next

    self.first = None

    previous.next = current.next

    # Delete the nth link starting from the Link start
    # Return the next link from the deleted Link
  def delete_after(self, start, n):
    current = self.find(start)

    for i in range(n - 1):
      current = current.next

      # print statement?

      self.delete(current.data)
      return (current.next)

    # Return a string representation of a Circular List
  def __str__(self):
    current = self.first
    soilderStr = ''

    while (current.next != self.first):
      soilderStr += str(current.data) + ' '
      current = current.next

    return soilderStr


def main():
  in_file = open('josephus.txt', 'r')

  totalSoilders = int(in_file.readline())
  start = int(in_file.readline())
  num = int(in_file.readline())

  soilderList = CircularList()

  for i in range(1, totalSoilders + 1):
    soilderList.insert(i)

  soilderStr = ''

  for j in range(1, totalSoilders + 1):
    flag, start = soilderList(start, num)
    soilderStr += (str(flag) + '\n')

  print(soilderStr)


main()
