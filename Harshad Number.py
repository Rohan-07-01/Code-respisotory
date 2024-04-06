Num = int(input("Enter the number:"))

Sum =0
temp = Num
if( Num < 1 or Num > 100):
    print("Invalid input");

else:
    while temp >0:
        REM = int(Num%10)
        Sum = Sum+REM
        temp=temp/10


if (Num % Sum != 0):
    print(-1);

else:
    print(Sum);
