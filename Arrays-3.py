x =input('Enter the number of  elemets of the array:')
x =int(x)

y =[]
print(y);

z =len(y)
print(z);


i=0
while z<x:
    val= input('Enter the element of the array:')
    y.append(val)
    z=z+1


    print(y);
while (1==1):
    a =input('Enter the element which you want to check in the array:')
    if a in y:
        print("The element is present in the array");
    else:
        b =input('Do you want to append the element into the array:')
        if (b.upper()=="YES"):
            
            y.append(a)
            print(y);
           
        else:
           print("The element is not appended");

    d=input('Do you want to continue:')
    if (d.upper()=="NO"):
        exit()
    else:
        continue
    

    
        





