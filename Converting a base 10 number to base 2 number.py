Number =input('Enter the base 10 number:')
Number =int(Number)
Q =int(Number)
Answer =""  #Google
R=int(0)


if (Number==1 or Number==0):
    print ("The binary number is==", Number);

else:
    if (Number>0):

        while (Q>1):
            R =Q%2
            Q=int(Q/2)
            Answer =Answer+str(R)

            
            
        Answer =Answer+"1"

        print ( Answer[::-1]) 

    else:
        print ("The binary number for this number does not exist");
