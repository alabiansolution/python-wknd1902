# To define a function

def greetings():
    print('Hello people')

# To call the function

greetings()

# To create a flexible function
def say_hello(name):
        print('Hello' + name)

say_hello(' Benedict')
say_hello(' Alabi')

# Create a function that has 3 different arguments including name , age and profession

def profile(name, age, occupation):
    print('My name is ' + name+ ', I am ' + str(age) + 'years old and a ' +occupation+' by profession' )
profile('Alabi', 25, 'businessman')
profile('Tunde', 27, 'trader')
profile('Mike', 45, 'teacher')
