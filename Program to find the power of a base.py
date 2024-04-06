x = input('Enter the base value:')
x =int(x)

n =input('Enter the power of the base:')
n =int(n)

if (n>0):
    print("The answer is", x**n);
elif (n==0):
    print("The answer is 1");
elif (n<0):
    Answer = pow(x, n)
    print("The answer is", Answer);
    
