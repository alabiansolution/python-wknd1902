#  To define a class in python
# function inside in a class is called method
# properties inside a class is called attributes
class Car():
    color = 'Yellow'
    wheels= 4
    doors = 4

    #  define a function in a class using 'self'

    def detail(self):
        detail = 'The color of this car is {} with {} and {} doors'.format(self.color, self.wheels, self.doors)
        return detail

bmw = Car()
print(bmw.color)
print(bmw.detail())

#  For python use capital letter for class

mazda = Car()
mazda.color = 'green'
mazda.doors = 2
print(mazda.color)
print(mazda.detail())
