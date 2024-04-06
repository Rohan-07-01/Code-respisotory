COR=["VIOLET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"]
print(COR);
Colour =input('Enter the starting colour:')
Colour=Colour.upper()

Present=COR.count(Colour)
print(Present);

if (Present==1):

    x =COR.index(Colour)


    i=6
    while (i>0):
        print(COR[x-i])
        i=i-1

else:
    
    print("The colour inputted is not within COR");
