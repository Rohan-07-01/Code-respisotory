BNumber =input('Enter the binary number consisting only 0 and 1:')
isBinary =int(1) #Google
intNumber =int(0) #Google

print(str(BNumber))

for x in BNumber:
    if (x!="0" and x !="1"):
        isBinary=0
        break

if (isBinary==1):
    print("The number is a valid binary Number");

    los=len(BNumber)
    k=int(los)

    for x in BNumber:
        intNumber=intNumber + int(x)*2**(k-1)
        k=k-1

    print(intNumber);

else:
    print("The number is not a valid binary number");
