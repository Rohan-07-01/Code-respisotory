import math

A =input('Enter the first side:')
B =input('Enter the second side:')
C =input('Enter the third side:')

A =int(A)
B =int(B)
C =int(C)

S =(A+B+C)/2

if (A<=0 or B<=0 or C<=0):
    print("The area of the triangle is not defined");

else:
    print("The semi perimeter of the triangle is =", S);
    
    print("The area of the tringle is =", math.sqrt(S*(S-A)*(S-B)*(S-C)));
