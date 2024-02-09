# 2. Develop a program that prompts the user to enter their current temperature in Celsius and 
# prints out whether they should wear a jacket (if temperature is below 20°C) or not.
t = int(input('enter the temp : '))
if t < 20 :
    print(f'wear jacket temp is {t}c')
elif t > 20:
    print(f"everythin good")
else:
    print('invalid')