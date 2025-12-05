'''
Abstraction in python is the concept of hiding the complex implementation details
and showing only the essential features of the object. It helps in reducing
complexity and increases efficiency by allowing the user to focus on interactions
at a higher level.
'''

from abc import ABC, abstractmethod
# Abstract Base Class
class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount):
        pass

    def refund(self, amount):
        return f"Refunded {amount}"


# Derived class implementing the abstract method
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."
    
    
# Another derived class implementing the abstract method
class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal."
    
# Creating instances of the derived classes
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()
print(credit_card_payment.pay(100))  # Output: Paid 100 using Credit Card.
print(paypal_payment.pay(200))        # Output: Paid 200 using PayPal.
print(credit_card_payment.refund(50)) # Output: Refunded 50


