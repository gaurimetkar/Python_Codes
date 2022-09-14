"""A program to find the greatest of three numbers."""

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
max = 0

# method 1
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

# method 2
if num1 >= num2:
    if num1 >= num3:
        print(num1)
elif num2 >= num1:
    if num2 >= num3:
        print(num2)
else:
    print(num3)

# method 3
max = num1 if num1 > num2 else num2
max = num3 if num3 > max else max
print(max)
