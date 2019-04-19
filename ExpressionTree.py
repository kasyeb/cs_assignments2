#  File: ExpressionTree.py

#  Description: Using tree data strucutre to solve arthicmatic problems

#  Student's Name: Vinayak Sahal

#  Student's UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/16/2019

#  Date Last Modified:


class Stack (object):
  def __init__(self):
    self.stack = []

  def push(self, item):
    self.stack.append(item)

  def pop(self):
    return self.stack.pop()

  def peek(self):
    return self.stack[-1]

  def is_empty(self):
    return len(self.stack == 0)

  def size(self):
    return (len(self.stack))


class Node (object):
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None


class Tree (object):
  def __init__(self):
    self.root = None # Node(None)

  def create_tree(self, expr):

  def evaluate(self, aNode):
    if (aNode.data == '+'):
      return (self.evaluate(aNode, leftChild) + self.evaluate(aNode, rightChild))

    elif (aNode.data == '-')
      return (self.evaluate(aNode, leftChild) - self.evaluate(aNode, rightChild))

    elif (aNode.data == '*')
      return (self.evaluate(aNode, leftChild) * self.evaluate(aNode, rightChild))

    elif (aNode.data == '/')
      return (self.evaluate(aNode, leftChild) / self.evaluate(aNode, rightChild))

  def pre_order(self, aNode):

  def post_order(self, aNode):


def main():


main()
