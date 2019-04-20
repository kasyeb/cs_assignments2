#  File: ExpressionTree.py

#  Description: Using tree data strucutre to solve arthicmatic problems

#  Student's Name: Vinayak Sahal

#  Student's UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/16/2019

#  Date Last Modified: 4/19/2019

# Stack class


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
    return (len(self.stack) == 0)

  def size(self):
    return (len(self.stack))

# node class with two children


class Node (object):
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

# Tree class with None root


'''
Mitra Notes
If the current token is a left parenthesis add a new node as the left child of the current node. Push current node on the stack and make current node equal to the left child.
If the current token is an operator set the current node's data value to the operator. Push current node on the stack. Add a new node as the right child of the current node and make the current node equal to the right child.
If the current token is an operand, set the current node's data value to the operand and make the current node equal to the parent by popping the stack.
If the current token is a right parenthesis make the current node equal to the parent node by popping the stack if it is not empty.
'''


class Tree (object):
  def __init__(self):
    self.root = Node(None)

  def create_tree(self, expr):
    equation = expr.split()  # split operands with operators
    current = self.root
    operators = ['+', '-', '*', '/']
    operands = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    equationStack = Stack()

    for item in equation:
      if (item == '('):
        equationStack.push(current)
        current.leftChild = Node(None)
        current = current.leftChild

      elif (item in operators):
        current.data = item
        equationStack.push(current)
        current.rightChild = Node(None)
        current = current.rightChild

      elif (item.isdigit() or '.' in item):
        current.data = item
        current = equationStack.pop()

      elif (item == ')'):
        if (not equationStack.is_empty()):
          current = equationStack.pop()

        break

# perform actions of operands
  def evaluate(self, aNode):
    operands = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    if (aNode.data == '+'):
      return (self.evaluate(aNode.leftChild) + self.evaluate(aNode.rightChild))

    elif (aNode.data == '-'):
      return (self.evaluate(aNode.leftChild) - self.evaluate(aNode.rightChild))

    elif (aNode.data == '*'):
      return (self.evaluate(aNode.leftChild) * self.evaluate(aNode.rightChild))

    elif (aNode.data == '/'):
      return (self.evaluate(aNode.leftChild) / self.evaluate(aNode.rightChild))

    # elif (aNode.data.isdigit() or '.' in aNode.data):
    #   return eval(aNode.data)

# recursive method root - left - right
  def pre_order(self, aNode):
    if (aNode != None):
      print(aNode.data, end=' ')
      self.pre_order(aNode.leftChild)
      self.pre_order(aNode.rightChild)

# recursive method left - right - root
  def post_order(self, aNode):
    if (aNode != None):
      self.post_order(aNode.leftChild)
      self.post_order(aNode.rightChild)
      print(aNode.data, end=' ')


def main():
  in_file = open('expression.txt', 'r')
  equation = in_file.readline()
  expressionTree = Tree()

  expressionTree.create_tree(equation)

  print(equation, '=', expressionTree.evaluate(expressionTree.root))
  print('Prefix Expression: ', end='')
  expressionTree.pre_order(expressionTree.root)
  print('\n')
  print('Postfix Expression: ', end='')
  expressionTree.post_order(expressionTree.root)


main()
