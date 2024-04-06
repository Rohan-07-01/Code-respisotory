import math


F1 = input('Enter the value of the first force:')
F2 = input('Enter the value of the second force:')
costheta = input('Enter the cosine of the angle between the 2 forces:')

F1 = int(F1)
F2 = int(F2)
costheta = float(costheta)

if (F1<=0 or F2<=0 or costheta<0):
    print("The entered data is invalid");
elif(costheta==90):
    
    print("The resultant of the forces is 0");
else:
    
    Resultant=math.sqrt((F1**2)+(F2**2)+(2*F1*F2*costheta));

    print("The resultant of the 2 forces is", Resultant);
    
