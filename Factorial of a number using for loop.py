Num = input('Enter the number:')
Num = int(Num)

if (Num<0):
    print("The factorial of the number does not exist");
elif(Num==0):
    print("The factorial of the number is 1");

else:
    i=1
    Factorial=1
    for i in range(1,Num+1):
        Factorial = Factorial*i
        i=i+1

    print("The factorial of the number is", Factorial);
