import math

x1 = input('Enter the x value of the first point:')
y1 = input('Enter the y value of the first point:')

x2 = input('Enter the x value of the second point:')
y2 = input('Enter the y value of the second point:')

x3 = input('Enter the x value of the third point:')
y3 = input('Enter the y value of the third point:')

x1 = int(x1)
y1 = int(y1)

x2 = int(x2)
y2 = int(y2)

x3 = int(x3)
y3 = int(y3)

Area=[x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)]



print("The area of the triangle is", Area);
