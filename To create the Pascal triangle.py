Range =input("Enter the maximum number:")
Range =int(Range)
print("The range inputted is", Range);


if (Range<=0):
    print("The range inputted is invalid");
else:
    print("The range inputted is valid");

if (Range==1):
    print("1");

else:
    Line=1
    i=1
    NumValsInLine=1
    while i<=Range:
        print("\n\t", i, end=" ");
        i=i+1
        
        while NumValsInLine<Line:
            if (i>Range):
                break
            print("\t", i, end=" ");
            i=i+1
            
            NumValsInLine=NumValsInLine+1

        NumValsInLine=1
        print("\t", "Line=",Line, end=" ");
        Line=Line+1
                        
          

            
                       
                        
                  
