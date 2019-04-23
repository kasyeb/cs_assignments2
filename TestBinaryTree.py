class Node (object):
  ...

class Tree (object):
  # Returns the height of the tree
  def get_height (self, aNode): 

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self, aNode):

  # returns the difference between the height of the left
  # sub tree and the height of the right sub tree
  def balance_factor (self, aNode):

  # returns True if the tree is balanced and False otherwise
  # in a balanced tree every node has a balance factor of -1, 0, 1
  def is_balanced (self, aNode):

  # create a balanced binary search tree from a sorted list
  def create_tree (self, a_list):

  # prints the nodes breadth first 
  def print_level (self, aNode):

def main():
    # Create at least two binary search trees - one balanced and
    # the other not

    # Test your function get_height() for those trees

    # Test your function num_nodes() for those trees 

    # Find the balance factors of the roots of those trees

    # Find if the trees are balanced or not

    # Create a balanced binary search tree from a sorted list
    # check that it is balanced

    # Print all the trees that you have breadth first
