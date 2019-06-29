class Animal():

    location = 'Ocean'
    type = 'fish'

    def __init__(self, name, weight, skeleton, eyelid=True):
        self.name = name
        self.weight = weight
        self.skeleton = skeleton
        self.eyelid = eyelid

    def details(self):
        if self.eyelid == True:
            return 'The name of this animal is {} and is weighing {}  is of a type {} with an eyelid and a {} skeleton '.format(self.name, self.weight, self.type, self.skeleton)
        else:
            return 'The name of this animal is {} and is weighing {}  is of a type {} with no eyelid and a {} skeleton '.format(self.name, self.weight, self.type, self.skeleton)

    def __str__(self):
        return self.name+' '+self.skeleton

p1 = Animal('Sammy', 50, 'Cartilage', True)

print(p1)
