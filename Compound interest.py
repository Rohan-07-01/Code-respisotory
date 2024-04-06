Principal =input('Enter the principal:')
Rate =input('Enter the rate:')
Time =input('Enter the time period:')
Frequency =input('Enter the frequency of interest calculation:')

Principal=float(Principal)
Rate =float(Rate)
Time = float(Time)

print (Frequency.upper()) # Debug statement

if (Frequency.upper()=="YEARLY"):
    Ratemultiplier=1
    
if (Frequency.upper()=="HALFYEARLY"):
    Ratemultiplier=2
    
if (Frequency.upper()=="QUARTERLY"):
    Ratemultiplier=4
    
if (Frequency.upper()=="WEEKLY"):
    Ratemultiplier=52
    
if (Frequency.upper()=="DAILY"):
    Ratemultiplier=365



if (Principal<=0 or Rate<=0 or Time<=0):
    print ("The amount is not defined");
else:
    CIAmount=Principal * (1+Rate/100)**(Time*Ratemultiplier)
    print ("The CI Amount=", CIAmount, "CI=", CIAmount-Principal );

    SI =Principal*Time*Rate/100
    print ("The SIAmount=",  Principal+ SI, "SI=",SI);
           

    

    


