# class device:
#     def poweron(self):
#         print("device switched on")
# class phone(device):
#     def call(self):
#         print("make a phone call")
# class computer(device):
#     def program(self):
#         print("run a python program")
# samsung=phone()
# samsung.poweron()
# samsung.call()
# hp=computer()
# hp.poweron()
# hp.program()

# class phone:
#     def camera(self):
#         print("taking a nomral photo")
# class smartphone(phone):
#     def camera(self):
#         print("taking a pictrait photo")
# samsung=smartphone()
# samsung.camera()
# nokia=phone()
# nokia.camera()

# class bank:
#     __amount=800
#     def printamount(self):
#         return self.__amount
# hdfc=bank()
# print(hdfc.printamount())

# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(payment):
#     def pay(self):
#         print("payment done using upi")
# class phonepe(payment):
#     def pay(self):
#         print("payment done using phonepe")
# Payment=UPI()
# Payment.pay()
# Payment=phonepe()
# Payment.pay()