# 1. Calorie Counter: Write a program that asks the user for their 
# age, weight, and activity level, then calculates their daily 
# calorie goal based on recommended guidelines. Use ifelse state

age = int(input('Enter the age : '))
weight = int(input('Enter the weight : '))
activity_level = int(input('Enter activity level 1 to 10 : '))
if age > 10 :
    if weight > 60 and weight < 80 :
        print('Your cal goal is 120 calories per day ')
    elif weight < 60 :
        print('your cal goal is 200 calories per daay ')
    else:
        print('your over wieghted eat less ')
elif age > 20 and age < 31 :
       if weight > 70 and weight < 90 :
          print('Your cal goal is 100 calories per day ')
       elif weight < 60 :
          print('your cal goal is 210 calories per daay ')
       else:
          print('your over wieghted eat less ')
else:
    print('your old just take care of ur self :-) ')