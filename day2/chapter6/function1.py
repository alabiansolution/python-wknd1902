def add_range(min, max):
    total = 0
    increase = max+1
    for x in range(min, increase):
        total += x
    print(total)

add_range(1, 3)



def print_even(min, max):
    for x in range(min, max):
        if x % 2 == 0:
            print(x)

print_even(1, 21)
