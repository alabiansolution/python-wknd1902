# 1. Create a multiplication table program using while loop, this will be done in such a way that when a
# user supplies any number the multiplication table of that number will be created.

start = int(input('Enter start number: '))
num = int(input('Enter number: '))
while start <= 12:
    print(num, ' X ', start, ' = ', num*start)
    start += 1
