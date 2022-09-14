"""A program to find the sum of first n natural numbers."""

number,sum = 6,0    # here n=6, we'll find sum of first 6 natural numbers.

# method 1
for i in range(number+1):
  sum+=i
print(sum)

# method 2: using formula to find sum of n terms
sum = int((number * (number + 1))/2)
print(sum)

# method 3: using recursion
def recursum(number):
  if number == 0:
    return number
  return number + recursum(number-1)
print(recursum(number))
