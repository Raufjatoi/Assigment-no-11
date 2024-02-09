# 6. Implement a program that takes a user's input of a year and month and prints out the number 
# of days in that month, considering leap years

def days_in_month(year, month):
  months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  return months[month - 1] + (month == 2 and is_leap_year(year))

def is_leap_year(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter a year: "))
month = int(input("Enter a month number (1-12): "))

if month < 1 or month > 12:
  print("Invalid month number. Please enter a number between 1 and 12.")
else:
  num_days = days_in_month(year, month)
  print("The month", month, "in year", year, "has", num_days, "days.")
