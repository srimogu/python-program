# def fib(n,a,b):
#     if n==0:
#         return 
#     c=a+b 
#     print(c,end=" ")
#     a=b 
#     b=c 
#     fib(n-1,a,b)

# print("0","","1",end=" ")
# fib(10,0,1)

# def count(num):
#     if num==11:
#         return 1
#     print(num,end=" ")
#     count(num-1)
# count(1)

# a=0
# b=0
# print(a," ",b,end=" ")
# for i in range(3,11):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
# print()
# def fib(num):
#     if num==0 or num==1:
#         return num
#     return fib(num-1)+fib(num-2)

# num=int(input())
# print(fib(num))

# class studenttwo:
#     name="unknow"
#     mark=0
#     def display(self):
#         print(self.name," ",self.mark)

# class studentone:
#     name="naveen"
#     age=20
#     dept="ece"
#     def marks(self):
#         print("maths: 90 ,English: 78")

# class studentthree:
#     name="unknown"
#     mark=0
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark

#     def printdetails(self):
#         print(self.name," ",self.mark)

# s1=studentone()
# print(s1.name)
# print(s1.age)
# s1.marks()

# s2=studenttwo()
# s2.name="aravindh"
# s2.mark=345
# s2.display()

# s3=studenttwo()
# s3.name="dharshan"
# s3.make=456
# s3.display()

# s4=studentthree("kumar",43)
# s4.printdetails()

class device:
    def poweron(self):
        print("device switch on")
class phone(device):
    def call(self):
        print("making a phone call")
samsung=phone()
samsung.poweron()
samsung.call()
print()

class device:
    def power(self):
        print("device switched on")
class computer(device):
    def call(self):
        print("making a phone call")
class laptop(computer):
    def call(self):
        print("making a phone call")
