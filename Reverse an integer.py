x = int(input("Enter the number:"))

i=0

if(-(2**31) <= x <= (2**31)-1):

    while(x > 0):

        REM = int(x % 10)
        i= i * 10 + REM
        x = int(x/10)

    print(i);

else:
    print("Please enter a valid integer");
    
