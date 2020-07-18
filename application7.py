# understanding abstraction:
# hiding the complexity and only showing the essential features of the object.Hiding the real time
# implementation and as a user ,will be knowing only how to use it.
# ex: tv remote, car.

# Creditcard payment system, mobliewallet payment.
from abc import ABC, abstractmethod   #ABC-----> Abstract Base Class, abstractmethod # superclass

class Payment(ABC):
    def print_slip(self,Amount):
        print(f"Purshase of amount, {Amount}")
    @abstractmethod #------>template
    def payment(self, Amount):
        pass
class CreditCardPayment(Payment):
    def payment(self, amount):
        print(f"Credit card payment of - {amount}")
class MobileWalletPayment(Payment):
    def payment(self, amount):
        print(f"Mobile wallet payment of - {amount}")

obj=CreditCardPayment()
obj.payment(100)
obj.print_slip(100)

obj=MobileWalletPayment()
obj.payment(200)
obj.print_slip(200)



