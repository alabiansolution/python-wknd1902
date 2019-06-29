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


a1 = Animal('Sammy', 50, 'Cartilageous', True)
print(a1.details())

a2 = Animal('Simba', 70, 'Normal Skeleton', False)
a2.location = 'Forest'
a2.type = 'Beast'
print(a2.details())
