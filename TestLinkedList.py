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
      previous.next = new_link
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
      current = current.next
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
    # WRONG CHANGE IT - do some sorting algorithm
  def sort_list(self):
    new_list = LinkedList()
    current = self.first

    if (current == None):
      return None

    while (current != None):
      new_list.insert_first(current.data)  # new_list.insert_in_order(current.data)
      current = current.next

    return new_list

    # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted(self):
    current = self.first

    while (current.next != None):
      if (current.data <= current.next.data):
        current = current.next
      else:
        return False

    return True

    # Return True if a list is empty or False otherwise
  def is_empty(self):
    return (self.get_num_links() == 0)

    # Merge two sorted lists and return new list in ascending order
    # MIGHT BE WRONG CHECK - do some sorting algorithm
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

  print('Testing insert_first() and __str__(): ')
  print('Printing Linked List')
  print(testLinkedList1)

  # Test method insert_last()

  print('')
  testLinkedList2 = LinkedList()
  for i in range(20):
    testLinkedList2.insert_last(i)

  print('Testing insert_last(): ')
  print('Printing Linked List')
  print(testLinkedList2)

  # Test method insert_in_order()
  print('')
  testLinkedList3 = LinkedList()
  for i in range(20):
    testLinkedList3.insert_in_order(i)

  print('Testing insert_in_order(): ')
  print('Printing Linked List')
  print(testLinkedList3)

  # Test method get_num_links()
  print('')
  print('Testing get_num_links on testLinkedList1: ')
  print('Printing testLinkedList1.get_num_links()')
  print(testLinkedList1.get_num_links())

  # Test method find_unordered()
  # Consider two cases - data is there, data is not there
  print('')
  print('Testing find_unordered on testLinkedList1 if data is there: ')
  print('Printing testLinkedList1.find_unordered(10) != None')
  print(testLinkedList1.find_unordered(10))

  print('Testing find_unordered on testLinkedList1 if data is not there: ')
  print('Printing testLinkedList1.find_unordered(25) != None')
  print(testLinkedList1.find_unordered(25))

  # Test method find_ordered()
  # Consider two cases - data is there, data is not there
  print('Testing find_ordered on testLinkedList1 if data is there: ')
  print('Printing testLinkedList1.find_ordered(10) != None')
  print(testLinkedList1.find_ordered(10))

  print('Testing find_unordered on testLinkedList1 if data is not there: ')
  print('Printing testLinkedList1.find_unordered(25) != None')
  print(testLinkedList1.find_unordered(25))

  # Test method delete_link()
  # Consider two cases - data is there, data is not there
  print('')
  print('Testing delete_link() on testLinkedList1 if data is there: ')
  print('Printing testLinkedList1.delete_link(10)')
  print(testLinkedList1.delete_link(10))

  print('Testing delete_link on testLinkedList1 if data is not there: ')
  print('Printing testLinkedList1.delete_link(25)')
  print(testLinkedList1.delete_link(25))

  # Test method copy_list()
  print('')
  print('Testing copy_list() on testLinkedList1: ')
  print('Original list (testLinkedList1)')
  print(testLinkedList1)

  print('Copied list using copy_list')
  print(testLinkedList1.copy_list())

  # Test method reverse_list()
  print('')
  print('Testing reverse_list() on testLinkedList1: ')
  print('Original list (testLinkedList1)')
  print(testLinkedList1)
  print('Reversed testLinkedList1')
  print(testLinkedList1.reverse_list())

  # Test method sort_list()
  print('')
  testLinkedList4 = LinkedList()
  for i in range(20):
    randNum = random.randint(0, 19)
    testLinkedList4.insert_last(randNum)

  print('Testing sort_list() on testLinkedList4: ')
  print('Original list (not sorted)')
  print(testLinkedList4)
  print('Sorted list')
  print(testLinkedList4.sort_list())

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print('')
  print('Testing is_sorted() with testLinkedList4 (not sorted) and testLinkedList1 (sorted): ')
  print('testLinkedList1.is_sorted()')
  print(testLinkedList1.is_sorted())
  print('testLinkedList4.is_sorted()')
  print(testLinkedList4.is_sorted())

  # Test method is_empty()
  print('')
  print('Testing is_empty() on testLinkedList1 (not empty)')
  print(testLinkedList1.is_empty())

  # Test method merge_list()
  print('')
  testLinkedList5 = LinkedList()
  testLinkedList6 = LinkedList()

  for i in range(10):
    randNum = random.randint(0, 10)
    testLinkedList5.insert_last(randNum)

  for j in range(10):
    randNum = random.randInt(0, 10)
    testLinkedList6.insert_last(randNum)

  print('Testing merge_list() with testLinkedList5 and testLinkedList6: ')
  print('testLinkedList5')
  print(testLinkedList5)
  print('testLinkedList6')
  print(testLinkedList6)
  print('Merging both lists')
  print(testLinkedList5.merge_list(testLinkedList6))

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print('')
  print('Testing is_equal() with two lists: ')
  testLinkedList7 = LinkedList()
  testLinkedList8 = LinkedList()
  testLinkedList9 = LinkedList()

  for i in range(10):
    testLinkedList7.insert_last(i)

  for j in range(10):
    testLinkedList8.insert_last(j)

  for k in range(15):
    testLinkedList9.insert_last(k)

  print('Testing if testLinkedList7 and testLinkedList8 are equal (true)')
  print(testLinkedList7.is_equal(testLinkedList8))
  print('Testing is testLinkedList7 and testLinkedList8 are equal (false)')
  print(testLinkedList7.is_equal(testLinkedList9))

  # Test remove_duplicates()
  print('')
  testLinkedList10 = LinkedList()
  for i in range(20):
    randNum = randint(0, 5)
    testLinkedList10.insert_last(randNum)

  print('Testing remove_duplicates(): ')
  print('Orignal list')
  print(testLinkedList10)
  print('List after removing duplicates')
  print(testLinkedList10.remove_duplicates())


if __name__ == "__main__":
  main()
