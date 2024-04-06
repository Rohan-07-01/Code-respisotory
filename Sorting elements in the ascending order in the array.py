NumElements =input('Enter the number of  elemets of the array:')
NumElements =int(NumElements)

Array =[]
print(Array);

ArrayLen =len(Array)
print(ArrayLen);

Temp=0
i=0
j=0
while ArrayLen<NumElements:
    val= input('Enter the element of the array:')
    Array.append(val)
    ArrayLen=ArrayLen+1
    print(Array);

for i in range(0, ArrayLen):
    for j in range(i+1, ArrayLen):
        if (Array[i]>Array[j]):
            Temp = Array[i]
            Array[i] = Array[j]
            Array[j] = Temp

print(Array[i]);


