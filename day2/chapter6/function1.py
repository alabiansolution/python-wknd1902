def sum(num1, num2):
    print(num1 + num2)

sum(2, 4)

def add_range(min, max):
    total = 0
    increase = max + 1
    for x in range(min, increase):
        total += x
    print(total)

add_range(1, 5)

def even_num(min, max):
    for x in range(min, max):
        if x % 2 == 0:
            print(x)

even_num(1, 21)
