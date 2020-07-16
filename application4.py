# working with multiple inheritence.

class Dad:
    var1='hey i am var1'
    var2='hey i am var2'
    var3='hey i am var3'
class Mom:
    var4='hey i am mom'
class Child(Dad,Mom):
    pass

obj=Child()
print(obj.var4)