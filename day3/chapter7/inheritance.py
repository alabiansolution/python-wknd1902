# 4. Create a class called Bicycle list out the possible class properties of this Bicycle, create a method
# that will display the details of this Bicycle, create a method that will convert the weight in Kilogram
# (kg) to pounds (lbs) and another method that will convert pounds to kilogram make sure that
# weights are floats and rounded accordingly you can check the python documentation for some
# these functions. Where 1 kg = 2.20462 lbs
# a. Create an instance of this class
# b. Call the diiferent methods in this class

class Bicycle():
    name = 'BMW'
    color = 'Red'
    wheels = 2

    def details(self):
        return 'The name of this Bicycle is {} and the color is {} with {} wheels'.format(self.name, self.color, self.wheels)

    def kg_to_pounds(self, kg):
        pounds = 2.20462 * kg
        return pounds

    def pounds_to_kg(self, pounds):
        kg = pounds/2.20462
        return kg


class WheelBarrow(Bicycle):
    handle = 2
    wheel = 1

    def __init__(self, manufacturer, color):
        self.manufacturer = manufacturer
        self.color = color

    def wheel_detail(self):
        return 'This wheel barraow is manufactured by {} and it has a color of {}'.format(self.manufacturer, self.color)

w1 = WheelBarrow('Toyota', 'green')
print(w1.wheel_detail())
print(w1.pounds_to_kg(30))
