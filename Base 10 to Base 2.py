Number =input('Enter the number:')
Number =int(Number)


if (Number<0):
    print("The number is not possible");

else:
    Str=""
    Q=int(Number/2)
    while Q>0:

              
                REM=int(Number%2)
                Q=int(Q/2)
                Number=int(Number/2)
                
                Str=(Str+str(REM))

    Str=Str+str(Number)
    Str=Str[::-1]
    print(Str)
    

            
