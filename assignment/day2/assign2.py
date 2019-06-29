class Bicycle():
    color = "Yellow"
    wheels = 2
    sits = 1

    def detail(self):
        detail = ', The color of the Bicycle is {} with {} wheels and {} sit. '.format(self.color, self.wheels, self.sits)
        return detail

    def __int__(self, kg, lbs):
        self.kg = kg
        self.__lbs = lbs

    def input(self):
        self.kg = float(input('kg: '))

    def Calculator(self):
       self.weight = self.kg*2.20462


rec = Bicycle()
rec.input()
rec.Calculator()
mazda = Bicycle()
mazda.color= 'green'
mazda.wheels=4
print("The weight of the Bicycle is {}{} " .format(rec.weight, mazda.detail()))
