txt =input('Enter the txt:')

x =txt.isnumeric()
print(x)

i=0

if x==True:
        txt=int(txt)
        while txt>0:
            REM =int(txt%10)
            i =i*10+REM
            txt =int(txt/10)

        print(i);

else:
    print("Please enter a valid integer");
    
        
