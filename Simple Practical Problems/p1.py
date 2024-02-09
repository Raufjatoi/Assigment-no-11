# 1. Design a Python program that calculates the total cost of items purchased by a customer based 
# on the provided unit price and quantity, applying a discount of 10% if the total cost exceeds 
# $1000.

a = {'apple': 100, 'banana': 120, 'tomato':90}
print('What u want from the followin ')
print(a)
o = input('enter item : ').lower()
q = int(input('enter the quentity'))
total = a[o] * q
if total > 1000:
    print(f" total is {total*0.10}")
else:
    print(f'total is {total}')