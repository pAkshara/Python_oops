# understanding polymorphism. poly---many  and morphism---forms.
# is an ability to use a common interface for multiple forms.

class Parrot:
    def fly(self):
        print('parrot can fly')
    def swim(self):
        print('parrot cannot swim')
class Penguin:
    def fly(self):
        print('penguin cannot fly')
    def swim(self):
        print('penguin can swim')
# common interface.
def flying_test(bird):
    bird.fly()

# instantion of objects
par=Parrot()
pen=Penguin()

# passing the object.
flying_test(par)
flying_test(pen)

# common interface.
def swimming_test(bird):
    bird.swim()

# instantion of objects
par=Parrot()
pen=Penguin()

# passing the object.
swimming_test(par)
swimming_test(pen)
