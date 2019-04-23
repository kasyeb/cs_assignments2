#  File: BST_Cipher.py

#  Description: Encrypts and decrypts words

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/22/2019

#  Date Last Modified:

# Node class
class Node(object):
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

  def __str__(self):
    return str(self.data)

# Tree class
class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__(self, encrypt_str):
    self.root = None

    # make set to store all letters
    charSet = set('abcdefghijklmnopqrstuvwxyz')
    encrypt_str = encrypt_str.lower()

    # iterate each item check if it meets conditions listed
    for char in encrypt_str:
      if char in charSet or char == ' ':
        self.insert(char)
      else:
        continue

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert(self, ch):
    charSet = set('abcdefghijklmnopqrstuvwxyz')
    if (ch in charSet or ch == ' '):
      newNode = Node(ch)

    # base condition to see if empty
    if (self.root == None):
      self.root = newNode

    current = self.root
    parent = self.root

    # iterate through binary tree to check if slot open
    while (current != None):
      parent = current
      if (ch < current.data):
        current = current.leftChild
      elif (ch > current.data):
        current = current.rightChild

    if (ch < parent.data):
      parent.leftChild = newNode
    else:
      parent.rightChild = newNode

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
  def search(self, ch):
    emptyStr = ''
    current = self.root

    # see if it matches root
    if (current.data == ch):
      emptyStr += '*'

    # iterate through looking for data
    while (current.data != ch) and (current.data != None):
      if (ch < current.data):
        emptyStr += '<'
        current = current.leftChild
      elif (ch > current.data):
        emptyStr += '>'
        current = current.rightChild

    return emptyStr

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
  def traverse(self, st):
    current = self.root

    # iterate through and compare you can iterate through children properly
    for i in st:
      if (current == None):
        return ''
      elif (i == '<'):
        current = current.leftChild
      elif (i == '>'):
        current = current.rightChild
      elif (i == '*'):
        return self.root.data

    return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
  def encrypt(self, st):
    emptyStr = ''
    st = st.lower()
    charSet = set('abcdefghijklmnopqrstuvwxyz')

    # use set and iterate through all the items and encrypt the data
    for i in st:
      if (i in charSet or i == ' '):
        item = self.search(i)
        emptyStr = emptyStr + str(item) + '!'

    return emptyStr[:-1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
  def decrypt(self, st):
    emptyStr = ''
    st = st.split('!')

    # iterate through and find the value (traversing) and decrpt
    for i in st:
      emptyStr += self.traverse(i)

    return emptyStr


def main():
  key = 'the quick brown fox jumps over the lazy dog'
  encrpytionTree = Tree(key)
  print('Enter encryption key: the quixk brown fox jumps over the lazy dog')

  encryptionWord = input('Enter string to be encrypted: ')
  encrypt = encrpytionTree.encrypt(encryptionWord)
  print('Encrypted string: ' + str(encrypt))

  print('\n')

  decryptionWord = input('Enter string to be decrypted: ')
  decrypt = encrpytionTree.decrypt(decryptionWord)
  print('Decrypted string: ' + str(decrypt))


main()
