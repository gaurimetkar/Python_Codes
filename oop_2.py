# Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self, val):
        self.Value = val

    def ChkPrime(self):
        arr = self.Factors()
        if len(arr) == 2:
            return True

    def ChkPerfect(self):
        sum = self.SumFactors()
        if sum == self.Value:
            return True

    def SumFactors(self):
        arr = self.Factors()
        sum = 0
        for i in range(len(arr)-1):
            sum = sum + arr[i]
        return sum

    def Factors(self):
        arr = []
        for i in range(1, self.Value+1):
            if int(self.Value) % i == 0:
                arr.append(i)
        return arr

def main():
    obj1 = Numbers(61)
    obj2 = Numbers(28)

    obj1.ChkPrime()
    obj1.ChkPerfect()
    print("Sum of factors of the given number is :", obj1.SumFactors())
    print("Factors of the given number are :", obj1.Factors())

    if obj1.ChkPerfect() == True: print("Given number is perfect")
    else: print("Given number is not perfect")

    if obj1.ChkPrime() == True: print("Given number is prime")
    else: print("Given number is not prime")
    print()

    obj2.ChkPrime()
    obj2.ChkPerfect()
    print("Sum of factors of the given number is :", obj2.SumFactors())
    print("Factors of the given number are :", obj2.Factors())

    if obj2.ChkPerfect() == True: print("Given number is perfect")
    else: print("Given number is not perfect")

    if obj2.ChkPrime() == True: print("Given number is prime")
    else: print("Given number is not prime")
    print()

if __name__ == "__main__":
    main()