def add(var1, var2):
    sum = var1 + var2
    print(sum)

add(4, 6)
total = 0

# for x in range(1, 31):
#     total += x
#
# print(total)

def add_range(min, max):
    total = 0
    increase = max+1
    for x in range(min, increase):
        total += x
    print(total)

add_range(1, 3)

# for x in range(1, 21):
#     if x % 2 == 0:
#         print(x)

def print_even(min, max):
    for x in range(min, max):
        if x % 2 == 0:
            print(x)

print_even(1, 21)
