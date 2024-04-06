Num = input('Enter the number:')
Num = int(Num)

if (Num<0):
    print("Please enter a valid number");
elif (Num==0):
    print("The number of digiys is 1");

else:
    Count=0

    while Num>0:
        REM = int(Num%10)
        Q = int(Num/10)
        Num = Q
        Count = Count+1

print("The number of digits in the number is", Count);

    
