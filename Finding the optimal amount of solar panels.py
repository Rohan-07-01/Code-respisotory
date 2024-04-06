Area =input('Enter the square area of the plot:')
Area =int(Area)

if (Area<=0):
    print("Please enter a valid value");
elif (Area==1):
    print("WE need 1 solar panel of side 1");
else:
    print("The value inputted is valid");

    import math
    i=0
    while (1==1):
        while (Area>0):
            i=i+1
            SRoot = math.sqrt(Area)
            SRoot = int(SRoot)
            print("WE need 1 solar panel of side", SRoot, " covering an area of ", SRoot**2);
            RemArea = Area-(SRoot*SRoot)
            Area = RemArea
            
        print("WE need", i, "number of solar panels in total");


        UserResponse = input('Do you want to continue?')
        if (UserResponse.upper()=="YES"):
            Area =input('Enter the square area of the plot:')
            Area =int(Area)
        else:
            exit()

                
            

       

    

    

    
    

    



