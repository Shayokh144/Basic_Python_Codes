'''
class Variable
'''
class Student:
    schoolName = 'Baf Shaheen Kurmitola' # this is class var

s1 = Student()
print(s1.schoolName)
s2 = Student()
print(s2.schoolName)
s1.name = 'asif' # this is instace var, s2 cant access it
print(s1.name)



'''
Inheritance Example
'''

class Animal:
    state = "live"
    def __init__(self):
        pass
    def eat(self):
        print("animal has to eat ")


class Dog(Animal):
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def eat(self):
        print("{} eats anything".format(self.name))


dogObj = Dog("Tommy","small")
print(dogObj.state)
dogObj.eat()

class BullDog(Dog):
    def __init__(self):
        print("bulldog state={}".format(self.state))
        pass

bulldogObj = BullDog()
