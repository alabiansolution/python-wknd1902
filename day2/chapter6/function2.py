def office(name, color='Yellow'):
    print('The name of my office is ' + name + ' and the color is ' + color)

office('MTN')
office('Alabian', 'Blue')

def mult(multiply_by, multiplyer = 1, stop = 12):
    end = stop + 1
    for multiplyer in range(multiplyer, end):
        print(multiply_by, ' X ', multiplyer, ' = ',multiply_by*multiplyer)

mult(3)
mult(4, 5, 15)
