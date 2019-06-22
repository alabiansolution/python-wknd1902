# Write a program in python that tells if the name you supplied is in a list or
# the name is not in a list.

name = 'Tinubu'
capitalize = name.capitalize()
presidents = ['Buhari', 'Atiku', 'Sowore', 'Donald Duke']

if capitalize not in presidents:
    print('{} is not contesting for President'.format(capitalize))
    print('Here are list of presidential candidate')
    x = 0
    while x < len(presidents):
        print(presidents[x])
        x += 1
else:
    print('{} is contesting for President'.format(capitalize))
