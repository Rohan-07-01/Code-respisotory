x =input('Enter the number of elements on the aray:')
x =int(x)

y=[]
print(y);

z =len(y)
print(z);

i=0
while z<x:
    val =input('Enter the element of the array:')
    val=int(val)
    y.append(val)
    z=z+1

    print(y);

while (1==1):
    a =input('Enter the element which you want to delete in the array:')
    a=int(a)

    if a in y:
        y.remove(a)
        print (y)
    else:
        print("The element is not present in the array");

    d=input('Do you want to continue:')
    if (d.upper()=="NO"):
        exit()
    else:
        continue
        


