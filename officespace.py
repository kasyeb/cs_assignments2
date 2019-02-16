#  File: OfficeSpace.py

#  Description: Program that identifies overlapping spaces between employees and what empty spaces

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/14/2019

#  Date Last Modified:

import math


def totalArea(l, w):
    return l * w


def unallocatedArea():
    pass
    # return totalArea - usedArea


class Employee():
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.area = (x2 - x1) * (y2 - y1)

    def contestedSpace(self, e):  # strictly looks at overlap, if touching edges then its false
        return not((self.x2 <= e.x1) or (self.y2 <= e.y1) or (self.x1 >= e.x2) or (self.y1 >= e.y2))

    def contestedSpaceArea(self, e):
        a1 = abs(self.x1 - self.x2) * abs(self.y1 - self.y2)
        a2 = abs(e.x1 - e.x2) * abs(e.y1 - e.y2)

        intersectingArea = (min(self.x2, e.x2) - max(self.x1, e.x1)) * (min(self.y2, e.y2) - max(self.y1, e.y1))

        return (intersectingArea)


def getTotalContested(empList, newEmployee):
    contestedArea = 0
    for employee in empList:
        if employee.contestedSpace(newEmployee):
            employee.area -= employee.contestedSpaceArea(newEmployee)
            contestedArea += employee.contestedSpaceArea(newEmployee)
    print(contestedArea)
    return contestedArea


def main():

    with open('office.txt')
    file = open('office.txt', 'r')
    line1 = file.readline()
    officeLength = int(line1.split(' ')[0])
    officeWidth = int(line1.split(' ')[1])
    print('Total', totalArea(officeLength, officeWidth))

    empList = []
    numEmployees = int((file.readline()))

    for i in range(numEmployees):
        line3 = file.readline()
        employee = line3.split(' ')[0]
        x1 = line3.split(' ')[1]
        y1 = line3.split(' ')[2]
        x2 = line3.split(' ')[3]
        y2 = line3.split(' ')[4]
        newEmployee = Employee(x1,y1,x2,y2)

        if len(empList) < 1:
            empList.append()



    
    alice = Employee(2, 3, 10, 11)
    empList.append(alice)
    ted = Employee(7, 2, 18, 8)
    greedybob = Employee(17, 11, 30, 24)
    empList.append(greedybob)
    print(getTotalContested(empList, ted))
    empList.append(ted)


main()
