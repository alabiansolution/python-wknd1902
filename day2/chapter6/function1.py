def numbers(num1, num2):
    print(num1 + num2)

numbers (4,8)
numbers (6,8)
numbers (2,1)

def add_range(min, max):
    total = 0
    increase =max+1
    for x in range(1,4):
        total +=x
    print(total)
add_range (1,3)


def even_num(start, stop):
    for x in range (start, stop):
        if x % 2 == 0:
            print(x)
even_num (2,10)
