class Dog:
    """A simple attempt to design the dog class"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('it is getting initially')
    def sit(self):
        print(f"{self.name} is now sitting on the ground")
    def roll_over(self):
        print(f"{self.name} is now rolling over the command")
        print(f"{self.name} is of {self.age} years old")
    def sleep(self):
        print(f"{self.name} is now sleeping")

obj=Dog('snoopy',3)
obj.sit()
obj.roll_over()
obj.sleep()
