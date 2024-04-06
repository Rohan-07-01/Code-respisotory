N =input('Enter the range of elements:')
N =int(N)

if (N<0):
    print("The range is not defined");
else:
    print("The range is defined");

if (N==0):
    print("The sum and average of the elements is 0");
elif (N==1):
    print("The sum and average of elements is 1");
else:
    i=0
    Sum=0
    while i<=N-1:
        Elem = input('Enter the elements:')
        Elem = int(Elem)
        Sum =Sum+Elem
        i=i+1

print("The sum of elements is", Sum);

Average =float((Sum/N))
print("The average of the elements is", Average);
        
