#str1 = input('Please Enter String :')
str1 ="rOHaN"
str1 = "rU1x"


str2=""
y=[]
y=str1
print(y[1])
los=len(str1)
print(los)
i=0
while i<=los-1:
    if (i<los-1):
        if (y[i]>='a' and y[i]<='z' and y[i+1]>='A' and y[i+1]<='Z'):
             str2=str2+y[i+1]+y[i]+"*"
             i=i+2

        elif (y[i]>='1' and y[i]<='9'):
            str2=y[i]+str2+'0'          
            i=i+1
        else:
            str2=str2+y[i]
            i=i+1
            
       
    else:
        i=i+1

if (i<los):
        str2=str2+y[los-1]  

print(str2);
