def palindrome(str):
  palStr = ''
  for i in str:
    palStr = str + palStr
  
  return palStr

def palindrome1(str):
  return str[::-1]
