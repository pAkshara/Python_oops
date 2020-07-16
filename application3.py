# inmplimentation of inheritence.

class Parent:  # super class
    var1='hey i am var1'
    var2='hey i am var2'
    var3='hey i am var3'

class Child(Parent):
    pass # do nothing

obj=Child()
print(obj.var1)
print(obj.var2)
print(obj.var3)