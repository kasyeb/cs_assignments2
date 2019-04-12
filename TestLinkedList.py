#  File: TestLinkedList.py

#  Description: Linked list functions

#  Student Name: Vinayak Sahal

#  Student UT EID:  vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/9/2019

#  Date Last Modified: 4/12/2019

import random

class Link(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)


class LinkedList (object):
  def __init__(self):
    self.first = None

  # get number of links
  def get_num_links(self):
    count = 0
    current = self.first

    while (current != None):
      count += 1
      current = current.next

    return count

    # add an item at the beginning of the list
  def insert_first(self, data):
    new_link = Link(data)
    new_link.next = self.first
    self.first = new_link

    # add an item at the end of a list
  def insert_last(self, data):
    new_link = Link(data)
    # find the last link
    current = self.first
    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

    # add an item in an ordered list in ascending order
  def insert_in_order(self, data):
    new_link = Link(data)
    current = self.first
    previous = self.first

    if self.is_empty():
      self.first = new_link
      return

    while(current.data <= data):
      if (current.next == None):
        current.next = new_link
        return

      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.insert_first(data)
      return

    else:
      previous.next  = new_link
      new_link.next = current


    # search in an unordered list, return None if not found
  def find_unordered(self, data):
    current = self.first
    if (current == None):
      return None

    while (current != None):
      if (current.data == data):
        return current

      else:
        current = current.next

    return current

    # Search in an ordered list, return None if not found
  def find_ordered(self, data):
    current = self.first

    if self.is_empty():
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      elif (current.data.next > data):
        return None

      else:
        current = current.next

    return current


  def find_link(self, data):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

    # Delete and return Link from an unordered list or None if not found
  def delete_link(self, data):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

      if (current == self.first):
        self.first = self.first.next

      else:
        previous.next = current.next

    return current

    # String representation of data 10 items to a line, 2 spaces between data
  def __str__(self):
    dataStr = ''
    counter = 0
    current = self.first
    
    while (current != None):
      dataStr = dataStr + str(current.data) + ' '
      counter += 1

      if (counter % 10 == 0):
        dataStr = dataStr + '\n'

    return dataStr


    # Copy the contents of a list and return new list
  def copy_list(self):
    newList = LinkedList()
    current = self.first

    while (current != None):
      newList.insert_last(current.data)
      current = current.next

    return newList

    # Reverse the contents of a list and return new list
  def reverse_list(self):
    new_list = LinkedList()
    current = self.first

    while (current != None):
      new_list.insert_first(current.data)
      current = current.next

    return new_list


    # Sort the contents of a list in ascending order and return new list
  def sort_list(self):
    new_list = LinkedList()
    current = self.first

    if (current == None):
      return None

    while (current != None):
      new_list.insert_first(current.data)
      current = current.next

    return new_list


    # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted(self):
    sorted = True
    current = self.first

    while (current.next != None):
      if (current.data <= current.next.data):
        current = current.next
      else:
        sorted = False

    return sorted

    # Return True if a list is empty or False otherwise
  def is_empty(self):
    return (self.get_num_links() == 0)

    # Merge two sorted lists and return new list in ascending order
  def merge_list(self, other):
    new_list = LinkedList()
    selfCurrent = self.first
    otherCurrent = other.first

    while (selfCurrent != None):
      new_list.insert_in_order(selfCurrent.data)
      selfCurrent = selfCurrent.next

    while (otherCurrent != None):
      new_list.insert_in_order(otherCurrent.data)
      otherCurrent = otherCurrent.next

    return new_list

    # Test if two lists are equal, item by item and return True
  def is_equal(self, other):
    if (self.is_empty() and other.is_empty()):
      return True

    if (self.get_num_links() != other.get_num_links()):
      return False

    selfCurrent = self.first
    otherCurrent = other.first

    equalList = True
    while (selfCurrent != None and otherCurrent != None):
      if (selfCurrent.data == otherCurrent.data):
        selfCurrent = selfCurrent.next
        otherCurrent = otherCurrent.next

      else:
        equalList = False

    return equalList

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates(self):
    duplicatesList = LinkedList()
    duplicates = []
    current = self.first

    while (current != None):
      if (current.data in duplicates):
        pass
      
      else:
        duplicates.append(current.data)
        duplicatesList.insert_last(current.data)

      current = current.data

    return duplicatesList




def main():

  testLinkedList1 = LinkedList()

  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  for i in range(20):
    testLinkedList1.insert_first(i)

  print('Created new Linked List and insert_first integers from 0-19 in the list: ')
  print('Printing Linked List')
  print(testLinkedList1)


  # Test method insert_last()

  print('')
  testLinkedList2 = LinkedList()
  for i in range(20):
    testLinkedList2.insert_last(i)

  print('Created new Linked List and insert_last integers from 0-19 in the list: ')
  print('Printing Linked List')
  print(testLinkedList2)
  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered()
  # Consider two cases - data is there, data is not there

  # Test method find_ordered()
  # Consider two cases - data is there, data is not there

  # Test method delete_link()
  # Consider two cases - data is there, data is not there

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()



if __name__ == "__main__":
  main()
