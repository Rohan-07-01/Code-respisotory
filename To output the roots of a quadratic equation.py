a =input('Enter the coefficient of x2:')
b =input('Enter the coefficient of x:')
c =input('Enter the constant of the equation:')

import math
import cmath

a =int(a)
b =int(b)
c =int(c)

d =(b**2) - (4*a*c)

print("The discriminant of the equation is", d);

   
if (b**2-4*a*c>0):
    root1 =float(-b + math.sqrt(b**2 - 4*a*c))/2*a
    root2 =float(-b - math.sqrt(b**2 -4*a*c))/2*a
    print("The quadratic equation has 2 real and distinct roots");
    print("The first root is", root1);
    print("The second root is", root2);
elif (b**2-4*a*c==0):
    root =float(-b + math.sqrt(b**2 -4*a*c))/2*a
    print("The quadratic equation has double roots");
    print("The roots are ", root and root);

elif (b**2-4*a*c<0):
    root1 =(-b + cmath.sqrt(b**2 -4*a*c))/2*a
    root2 =(-b - cmath.sqrt(b**2 -4*a*c))/2*a
    print("The quadratic equation has complex roots");
    print("The first root is", root1);
    print("The second root is", root2);

