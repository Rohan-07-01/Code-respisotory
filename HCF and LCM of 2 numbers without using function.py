Num1 = input('Enter the first number:')
Num2 = input('Enter the second number:')

i = input('Enter the value of the HCF:')

Num1 = int(Num1)
Num2 = int(Num2)
i = int(i)

if (Num1%i==0 and Num2%i==0):
    print("The highest common factor between the 2 numbers is", i);

    LCM = (Num1*Num2)/i
    print("The Least common multiple between the 2 numbers is", LCM);

else:
    print("The highest common factor between the numbers is 1");
