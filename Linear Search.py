N = input('Enter the number of elements of the array:')
N = int(N)


arr =[];
print(arr);

Arraylen = len(arr)



while arr<N:
    val = input('Enter the elements of the array:')
    arr.append(val)
    Arraylen=Arraylen+1

print(arr);

key = input('Enter the element to be searched in the array:')
key = int(key)

for i in range(0, Arraylen):
    if(key==arr[i]):
        print("The element is present in the array");
        break;
    else:
        print("The element is not present in the array");
