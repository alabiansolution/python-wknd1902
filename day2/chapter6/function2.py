#To add a range

def add_range(min, max):
    total = 0
    increase = max+1
    for x in range(min, increase):
        total+= x
    print(total)

add_range(1, 10)

def even_numbers(min, max):
    for x in range(min, max):
        if x % 2 == 0:
           print(x)
even_numbers(1,21)
