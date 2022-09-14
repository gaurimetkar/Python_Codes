"""A program to find the sum of numbers in a given range."""

num1, num2 = 3, 6     # here the range is given i.e. 3 to 6
sum = 0

#method 1
for i in range(num1, num2+1):
    sum += i
print(sum)

#method 2
sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(sum)

#method 3
def recursum(sum, num1, num2):
    if num1 > num2:
        return sum
    return num1 + recursum(sum, num1 + 1, num2)

print(recursum(0, num1, num2))      # sum = 0
