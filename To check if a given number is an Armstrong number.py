Num =input('Enter the number:');
Num =int(Num)

    
if (Num<=0):
    print("The numeber is not defined");
else:
    Q=Num
    Arm=0
    while Q>0:
            REM =int(Q%10)
            Q =int(Q/10)
            
            Arm =REM**3+Arm

    print(Arm);

if (Arm==Num):
    print("The number is an Armstromg number");
else:
    print("The number is not an Armstromg number");
    
           
        
