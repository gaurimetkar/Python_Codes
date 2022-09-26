"""To check whether a number is prime or not."""

num = int(input("Enter the number:"))

# method 1: optimization by break condition
flag = 0
if num < 2:
    flag = 1
else:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

if flag:
    print(num, 'is not a Prime Number')
else:
    print(num, "is a Prime Number")

# method 2: optimization by n/2 iterations
flag = 0
if num < 2:
    flag = 1
else:
    for i in range(2, int((num/2) + 1)):
        if num % i == 0:
            flag = 1
            break

if flag == 1:
    print(num, 'is not a Prime Number')
else:
    print(num, "is a Prime Number")

# method 3: Optimization by skipping even iteration
flag = 0
if num < 2:
    flag = 1
elif num == 2:
    flag = 0
else:
    for i in range(3, int(pow(num, 0.5)+1), 2):
        if num % i == 0:
            flag = 1
            break

if flag == 1:
    print(num, 'is not a Prime Number')
else:
    print(num, "is a Prime Number")

# method 4: Basic Recursion technique
def checkPrime(num, iter=2):
    if num == iter:
        return True
    if num % iter == 0:
        return False
    if num < 2:
        return False
    return checkPrime(num, iter+1)

if checkPrime(num) == True:
    print(num, 'is a Prime Number')
else:
    print(num, 'is not a Prime Number')
