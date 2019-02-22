#  File: Palindrome.py

#  Description: Shortest palindrome by adding letters to the beginning of the word

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/22/2019

#  Date Last Modified: 2/22/2019

# naming function
def palindrome(strng):

  length = len(strng)
  revStr = ''

  # reverses string
  for i in strng:
    revStr = i + revStr

  # checks to see if input starts with reversered string and if it does it returns it
  for i in range(length + 1):
    if strng.startswith(revStr[i:]):
      return (revStr[:i] + strng)

# calling main
def main():

  # opening txt file
  with open('palindrome.txt') as file:
    for line in file:
      line1 = line.replace('\n', '')
      print(palindrome(line1))


main()
