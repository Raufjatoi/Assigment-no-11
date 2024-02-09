# 5. Develop a Python script that takes a user's input of a month (as a number) and prints out the 
# number of days in that month.

months = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31
}

while True:
  try:
    month_num = int(input("Enter a month number (1-12): "))
    if month_num < 1 or month_num > 12:
      raise ValueError("Invalid month number. Please enter a number between 1 and 12.")
    break
  except ValueError:
    print("Invalid input. Please enter a valid integer.")

days = months[month_num]
print(f"The month {month_num} has {days} days.")









































'''
months = {
  "January": 31,
  "February": 28,
  "March": 31,
  "April": 30,
  "May": 31,
  "June": 30,
  "July": 31,
  "August": 31,
  "September": 30,
  "October": 31,
  "November": 30,
  "December": 31
}

month_name = input("Enter a month name: "),Capatalize()

try:
  days = months[month_name]
  print(f"The month {month_name} has {days} days.")
except KeyError:
  print("Invalid month name. Please enter a valid month name.")
'''