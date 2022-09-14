"""check if number is positive or negative."""
no = int(input("Enter the number:"))

# method 1
if no == 0:
    print("zero")
elif no > 0:
    print("positive")
else:
    print("negative")

# method 2
if no >= 0:
    if no == 0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")

# method 3
print("positive" if no >= 0 else "negative")
