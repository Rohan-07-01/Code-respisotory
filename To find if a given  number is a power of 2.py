Num = input('Enter the even number:')
Num = int(Num)

if (Num<0):
    print("Please enter a valid number");
else:
    print("The number inputted is valid");
        

    if (Num%2!=0):
        print("The number inputted is an odd number and can't be a power of 2");

    else:
        print("The number inputted is an even number");

        while Num>1:
            REM = (Num%2)
            Q = (Num/2)
            Num = Q
        print("The quotient is", Q);

        if (Q==1):
            print("The number is a power of 2");
        else:
            print("The number is not a power of 2");
            

