ggclass Car():
    color = "Yellow"
    wheels = 4
    doors = 4

    def detail(self):
        detail = 'The color of this car is {} with {} wheels and {}  doors '.format(self.color, self.wheels, self.doors)
        return detail

bmw = Car()
print(bmw.color)
print(bmw.detail())

mazda = Car()
mazda.color='green'
mazda.doors=2
print(mazda.color)
print(mazda.detail())
