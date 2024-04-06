x =input('Enter the maximum number:')

y=[]
x =int(x)

if (x<=0 or  x>10**4):
    print("The number is not defined");
    exit()
i=1
i=int(i)

while i<=x:
        
        
        if (i%3==0 and i%7==0):
            y.append("FizzBuzz")
            #print("FizzBuzz");
        elif (i%3==0):
            y.append("Fizz")
            
            #print("Fizz");
        elif(i%7==0):
            y.append("Buzz")
            #print("Buzz");
        else:
            y.append(i)
        i=i+1
        
print(y);
