class Pet:
    def Speak(self):
        print("Pet hasn't learned any sounds yet")

class Dog(Pet):
    def Speak(self):
        print("Bark!")

class Cat(Pet):
    def Walk(self):
        print("walk")
#    def Speak(self):
#        print("Meow!")

Dog = Dog()
Dog.Speak()

Cat = Cat()
Cat.Speak()

a, b = 1, 2

print(a)
print(b)
