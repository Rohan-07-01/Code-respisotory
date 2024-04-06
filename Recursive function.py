#Factorial of a number

def fac_recursion(k):

    if (k==1):
        return(k)
    else:
        Result=k*fac_recursion(k-1)

    return(Result)

        


k =input("Enter the value of k:");
k =int(k)

if (k<0):
        print("The factorial is not possible");
else:
        print(fac_recursion(k));
        
