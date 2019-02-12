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

def main():
	file = open('geom-2.txt', 'r')
	line1 = file.readline()
	px = float(line1.split(' ')[0])
	py = float(line1.split(' ')[1])
	P = Point(px,py)
	print(P)

	line2 = file.readline()
	qx = float(line2.split(' ')[0])
	qy = float(line2.split(' ')[1])
	Q = Point(qx,qy)
	print(Q)

	print('Coordinates of P: ')
	print('Coordinates of Q: ')
	pqdist = P.dist(Q)
	print('Distance between P and Q: ', pqdist)

	line3 = file.readline()
	cr = float(line3.split(' ')[0])
	cx = float(line3.split(' ')[1])
	cy = float(line3.split(' ')[2])
	C = Circle(radius=cr, x=cx, y=cy)
	print(C)

	line4 = file.readline()
	dr = float(line4.split(' ')[0])
	dx = float(line4.split(' ')[1])
	dy = float(line4.split(' ')[2])
	D = Circle(radius = dr, x=dx, y=dy)
	print(D)

	print('Circle C: ')
	print('Cirlce D: ')
	print('Circumference of C: ')
	print('Area of D: ')


	line5 = file.readline()
	gux = float(line5.split(' ')[0])
	guy = float(line5.split(' ')[1])
	glx = float(line5.split(' ')[2])
	gly = float(line5.split(' ')[3])
	G = Rectangle(ul_x=gux, ul_y=guy, lr_x=glx, lr_y=gly)
	print(G)

	line6 = file.readline()
	hux = float(line6.split(' ')[0])
	huy = float(line6.split(' ')[1])
	hlx = float(line6.split(' ')[2])
	hly = float(line6.split(' ')[3])
	H = Rectangle(ul_x=hux, ul_y=huy, lr_x=hlx, lr_y=hly)
	print(H)


	

if __name__ == "__main__":
	main()
