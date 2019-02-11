#  File: Geom.py

#  Description: Collection of different classes

#  Student Name: Vinayak Sahal

#  Student UT EID: vs9736

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 2/10/2019

#  Date Last Modified: 2/11/2019

import math


class Point():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def dist(self, other):
    return math.hypot(self.x - other.x, self.y - other.y)

  def __str__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  def __eq__(self, other):
    tol = 1.0e-16
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle():
  def __init__(self, radius=1, x=0, y=0):
    self.radius = radius
    self.center = Point(x, y)

  def circumference(self):
    return 2.0 * math.pi * self.radius

  def point_inside(self, p):
    return(self.center.dist(p) < self.radius)

  def circle_inside(self, c):
    distance = self.center.dist(c.center)
    return(distance + c.radius) < self.radius

  def circle_overlap(self, c):
    return (((int(self.radius) - int(c.radius))^2) <= ((int(self.center.x) - int(c.center.x))^2) <=((int(self.radius) + int(c.radius))^2))

  def circle_circumscribe(self, r):
    circRadius = math.sqrt(((r.length())^2) + ((r.width())^2)) * (0.5)
    return circRadius
    # circCenter = 

  def __str__(self):
    return 'Radius ' + str(self.radius) + ', Center: ' + str(self.center)

  def __eq__(self, other):
    tol = 1.0e-16
    return ((abs(self.radius - other.radius) < tol) and (abs(self.radius - other.radius) < tol))


class Rectangle():
  def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point(ul_x, ul_y)
      self.lr = Point(lr_x, lr_y)
    else:
      self.ul = Point(0, 1)
      self.lr = Point(1, 0)

  def length(self):
    return abs(int(self.lr.x) - int(self.ul.x))

  def width(self):
    return abs(int(self.ul.y) - int(self.lr.y))

  def perimeter(self):
    return (2 * self.length()) + (2 * self.width())

  def area(self):
    return (int(self.length()) * int(self.width()))

  def point_inside(self, p):
    return ((self.ul.x < p.x < self.lr.x) and (self.lr.y < p.y < self.ul.y))

  def rectangle_inside(self,r):
    if ((self.ul.x < r.ul.x < self.lr.x) and (self.lr.y < r.lr.y < self.ul.y)):
      return True
    elif ((self.ul.x == r.ul.x) and (self.ul.y == r.ul.y) and (self.lr.x == r.lr.x) and (self.lr.y == r.lr.y)):
      return False
    else:
      return False

  def rectangle_overlap(self, r):
    return ((self.ul.x < r.lr.x) and (r.ul.x < self.lr.x) and (self.ul.y < r.ul.y) and (r.ul.y < self.ul.y))

  def rectangle_circumscribe(self, c):
    pass

  def __str__(self):
    return 'UL: ' + str(self.ul) + ', LR: ' + str(self.lr)

  def __eq__(self, other):
    return ((self.width() == other.width()) and (self.length() == other.length()))



# G = Rectangle(ul_x=2.0, ul_y=6.0,lr_x=8.0,lr_y=4.0)
# H = Rectangle(ul_x=-3.0, ul_y=2.0,lr_x=4.0,lr_y=-3.0)

# print(G.rectangle_inside(H))
