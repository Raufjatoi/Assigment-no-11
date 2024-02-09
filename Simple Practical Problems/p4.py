# 4. Create a program that simulates a simple ATM machine. It should ask the user for their PIN, 
# verify it, and then allow them to withdraw money if the balance is sufficient.
balance = 100000
pin = 1234
userpin = int(input('enter pin  :'))
if userpin == pin :
    print('correct pin , take money')
    a = int(input('enter amount to withdraw : '))
    if a <= balance:
        print(f' remanin balance is {balance-a}')
    elif a > balance:
        print(f"insufficent nbalance avaliable amount is {balance}")
else:
    print('incorrect pin ')
    