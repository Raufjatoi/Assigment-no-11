# 3. Write a Python script that takes a user's input of three sides of a triangle and determines 
# whether it is equilateral, isosceles, or scalene.

size1 = int(input('Enter the size of triangle 1 : '))
size2 = int(input('Enter the size of triangle 2 : '))
size3 = int(input('Enter the size of triangle 3 : '))
if size1 == size2 and size1 == size3:
    print('its equilateral triangle')
elif size1 == size2 or size1 == size2:
    print('its a isosceles trianle ')
else:
    print('its scalilne triangle ig ')