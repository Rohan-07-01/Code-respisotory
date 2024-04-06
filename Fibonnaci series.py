Range =input('Enter the maximum range:')
Range=int(Range)
print("The range inputted is", Range);

x=1
x=int(x)

y=1
y=int(y)

if (Range<=0):
    print("The given series is not possible");
elif (Range==1):
    print(x);
elif (Range==2):
    print(x,',',y);

else:
    i=1
    while i<=Range:
        print(x);

        nth=x+y
        x=y
        y=nth
        i=i+1
        


