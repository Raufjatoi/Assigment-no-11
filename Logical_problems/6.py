# 6. Create a program that asks the user to enter their exam score and prints out their grade based 
# on the following criteria: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
s = int(input('Enter exam score : '))
if s >= 90:
    print('A')
elif s >=80:
    print('B')
elif s >= 70:
    print('C')
elif s >= 60:
    print('d')
elif s <=59:
    print('f')
else:
    print('invalid')