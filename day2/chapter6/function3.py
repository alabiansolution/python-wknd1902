# default value
def mult(multiply_by, multiplyer=1, stop=12):
    end = stop + 1
    for multiplyer in (multiplyer, end):
        print(multiply_by, 'X', multiplyer, '=', multiply_by*multiplyer)

mult(3)
mult(4, 5, 15)
