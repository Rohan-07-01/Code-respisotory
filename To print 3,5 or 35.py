x =input("Enter the maximum value of x:")
x=int(x)

y=[]

i=1
i=int(i)

while i<=x:

        if(i%3==0):
            y.append("THREE")

        elif(i%5==0):
            y.append("FIVE")

        elif(i%3==0 and i%5==0):
            y.append("THREEFIVE")

        else:
            y.append(i)

        i=i+1

print(y)

