# understanding encapsulation
# we can be able to restrict the access to methods and attributesof the class.
# public access specitfiers.
# private access specitfiers.

class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(f"Selling price is :{self.__maxprice}")
    def setmaxprice(self,price):
        self.__maxprice=price

c=Computer()
#c.sell()

#change the price
#c.__maxprice=1000    #private access specifier
#c.sell()

#using the setter function.
c.setmaxprice(1000)     #this is only way that we can able to change the things
c.sell()