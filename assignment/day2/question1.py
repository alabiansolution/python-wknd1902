# Create a function in Python that will determine average of any numbers in a Python list.

numbers = [10, 15, 25, 35, 40]

total = 0

for number in numbers:
    total += number

average = total/len(numbers)
print(average)

def avg_list(list_numbers):
    total = 0
    for list in list_numbers:
        total += list
    avg = total/len(list_numbers)
    return avg

my_numbrs = [10, 20, 30, 40, 50]

print(avg_list(my_numbrs))
