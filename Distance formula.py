import math

x1 = input('Enter the x value of the first point:')
x2 = input('Enter the x value of the second point:')
y1 = input('Enter the y value of the first point:')
y2 = input('Enter the y value of the second point:')

x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

xf = int(x2-x1)**2
yf = int(y2-y1)**2

Value = xf+yf

print("The value of the point is", Value);

Distance = math.sqrt(Value);

print("The distance between the 2 points is", Distance);
