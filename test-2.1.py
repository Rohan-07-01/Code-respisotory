# Input the number
num = int(input("Enter a number: "))

# Calculate the sum of digits of the number
digit_sum = 0
temp = num
while temp > 0:
    digit_sum += temp % 10
    temp //= 10

# Check if the number is divisible by the sum of its digits
if num % digit_sum == 0:
    print(num, "is a Harshad number.")
else:
    print(num, "is not a Harshad number.")
