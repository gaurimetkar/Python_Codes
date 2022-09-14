"""A program to check whether the number is even or odd."""

no = int(input("Enter the number:"))

# method 1
if no % 2 == 0:
    print("even")
else:
    print("odd")

# method 2
print("even") if no %2 == 0 else print("odd")

# method 3
def isEven(no):
    return not no & 1
def main():
    if isEven(no):
        print('even')
    else:
        print('odd')

if __name__ == "__main__":
    main()
