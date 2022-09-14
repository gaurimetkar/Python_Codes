"""A program to find the greatest of two given numbers."""

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

# method 1
if num1 > num2:
    print(num1)
else:
    print(num2)

# method 2
print((num1 if num1>num2 else num2))

# method 3: using in-build max() function
print(max(num1,num2))
