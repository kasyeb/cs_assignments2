#  File: TestLinkedList.py

#  Description: Linked list functions

#  Student Name: Vinayak Sahal

#  Student UT EID:  vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/9/2019

#  Date Last Modified:


class Link(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class LinkedList (object):
  def __init__(self):
    self.first = None

  # get number of links
  def get_num_links(self):

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

    # search in an unordered list, return None if not found
  def find_unordered(self, data):

    # Search in an ordered list, return None if not found
  def find_ordered(self, data):

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

    # Copy the contents of a list and return new list
  def copy_list(self):

    # Reverse the contents of a list and return new list
  def reverse_list(self):

    # Sort the contents of a list in ascending order and return new list
  def sort_list(self):

    # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted(self):

    # Return True if a list is empty or False otherwise
  def is_empty(self):

    # Merge two sorted lists and return new list in ascending order
  def merge_list(self, other):

    # Test if two lists are equal, item by item and return True
  def is_equal(self, other):

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates(self):


def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  # Test method insert_last()

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
