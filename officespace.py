#  File: OfficeSpace.py

#  Description: Program that identifies overlapping spaces between employees and what empty spaces  

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/14/2019

#  Date Last Modified:


def totalArea(l, w):
    return l * w 

def unallocatedArea():
    pass
    # return totalArea - usedArea

def contestedArea():
    pass
    # 
    # for i in range((num from txt file)):


class Employee():
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.area = (x2-x1)*(y2-y1)

    def contestedArea(self, e): #strictly looks at overlap, if touching edges then its false
        return not((self.x2 <= e.x1) or (self.y2 <= e.y1) or (self.x1 >= e.x2) or (self.y1 >= e.y2))









def main():
    alice = Employee(2,3,10,11)
    ted = Employee(7,2,18,8)
    print(alice.contestedArea(ted))



main()
