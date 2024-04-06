Number =input('Enter the number:')

Number =int(Number)

answer=Number

if (Number==0):
    print (1);
else:

    while Number>1:
        answer=answer*(Number-1)
        Number=Number-1

    print (answer)
