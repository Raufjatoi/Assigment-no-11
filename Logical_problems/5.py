# 5. Implement a program that takes a user's input of three numbers and prints out the maximum 
# and minimum among them
a = []
for i in range(3):
    i = int(input('Enter a num : '))
    a.append(i)
print(a)
max1 = a [0]
min1 = a [-1]
for num in a :
    if num > max1:
        max1 = num
    elif num < min1:
        min1 = num
print(f'largest num is {max1}')
print(f'smallest one is {min1}')   
