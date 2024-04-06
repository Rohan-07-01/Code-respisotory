NumElementsInArr =input('Enter the number of elements in the array:')
NumElementsInArr =int(NumElementsInArr)

MyArr =[]
print(MyArr);

ArrLen =len(MyArr)
print(ArrLen);


while ArrLen<NumElementsInArr:
    value =input('Enter the element of the array:')
    MyArr.append(value)
    ArrLen=ArrLen+1

    print(MyArr);

while (1==1):
    VAL =input('Enter the element which you want to insert in the array:')
    if VAL in MyArr:
        print("The element is present in the array");
    else:
        POS =input('Specify the position where you want to insert the element:')
        POS =int(POS)
        MyArr.insert(POS, VAL)
        print(MyArr);

    UserInput =input('Do you want to continue:')

    if (UserInput.upper()=="NO"):
        exit()
    else:
        continue
