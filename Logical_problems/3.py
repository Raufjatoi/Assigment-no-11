# 3. Develop a program that prompts the user to enter two numbers and prints out the larger of the 
# two.
num = []
for i in range (1,3):
    a = int(input("input num: "))
    num.append(a)
if num[0] > num[1]:
        print(f"{num[0]} is larger")
elif num[1] > num[0] :
        print(f"{num[1]} is larger")
else:
        print('both are equal')