Number =input('Enter the number for which we need the table:')
Num2 =input('Enter the number of rows:')

Number =int(Number)
Num2 =int(Num2)

i=1

if (Number==0 or Num2<=0):
    print ("The multiplication table does not exist");
else:
    

    while i<=Num2:
       print(Number, "X", i, "=", Number*i)
       i=i+1

    

