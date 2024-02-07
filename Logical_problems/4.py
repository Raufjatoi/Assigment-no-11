# 4. Write a Python script to determine whether a given year is a leap year or not.
num = int(input("Enter year: "))

if num % 4 == 0:
    print(f'{num} is a leap year')
else:
    print(f'{num} is not a leap year')
