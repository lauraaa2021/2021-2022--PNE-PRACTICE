# instantiating an object

class Dog:
    def __init__(self, the_name, the_age):
        self.name = the_name
        self.age = the_age

# a class does not only have the data but also the methods, what does the dog can do inside our program

    def say_your_name(self):
        print("I´m {} , and I´m sitting down here".format(self.name))

    def show_your_age(self):
        print("I´m {} years old".format(self.age))

    def what_you_like(self):
        print("I like aritmetic")

    def multiply(self, first_operand, second_operand):
        print("The result is", first_operand * second_operand)

ares = Dog("ares", 10)
ares.say_your_name()
ares.show_your_age()
ares.what_you_like()
ares.multiply(3,5)
#ares.multiply() can´t go because you are not passing enough attributes or parameters to the function or method

#self is the own object so ares directly










# when we do ares = Dog("ares" , 10)
# we are instantiating or creating an object, so if we put dog python is going to look for class Dog which is being defined above
# so is going to look for that method and each class has that method or behavoiur and executes inside the class
# this is a mehtod that requires 2 parameters needed in order to create some variables or paraemters internal for the class
#those parameters are defined in self.name etc, for every dog in the system we need a name and an age, and we can modifciate it as we want
# Thats the data that eery dog will have following the template.
# So ARES will have a name said inside dog which is ares and the age which is 10
# so in dog ("ares and 10 ) are passed as arguments of the name and age of the function definin class.
# imagine we have another dog from another person called toby, which will be another object in the system of the class dog and as such will have an age and a number by passing the name and age of the parameters