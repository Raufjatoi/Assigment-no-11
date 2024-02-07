# 2. Create a program that asks the user to enter their age and prints out whether they are a child, 
#teenager, adult, or senior citizen.
age = int(input('enter your age please : '))
if age >25:
    print('Your senior citizen')
elif age >= 18:
    print("Your adult ")
elif  age >= 15 :
    print('your teenager')
else:
    print('youe child')