Num1 =input('Enter the first number:')
Num2 =input('Enter the second number:')

Num1 =int(Num1)
Num2 =int(Num2)

if (Num1<=0 or Num2<=0):
    print("The HCF and LCM of the numbers is not defined");
else:
    print("The HCF and LCM of the numbers is defined");

    def compute_hcf(Num1, Num2):
       while(Num2):
           Num1, Num2 = Num2, Num1 % Num2
       return Num1

    Hcf = compute_hcf(Num1, Num2)
    print("The HCF is", Hcf);

    Lcm = (Num1*Num2)/Hcf
    print("The Lcm of the 2 numbers is", Lcm);

    
