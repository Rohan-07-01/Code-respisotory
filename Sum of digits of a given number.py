Num = input('Enter the number:')
Num = int(Num)

Sum=0
while Num>0:
        REM = int(Num%10)
        Q = int(Num/10)
        Sum = Sum+REM
        Num = Q

print("The sum of the digits of the given number is", Sum);
