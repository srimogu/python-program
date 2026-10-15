

# bitwise operator( & | ^ << >>)

# a=int(input("give the value a:"))
# b=int(input("give the value b:"))
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(a << 1)
# print(b >> 1)

# ternary operator (other form of if else)

# a=int(input("enter the value:"))
# b="even" if a%2==0 else "odd"
# print(b)

# if(a%2==0):
#     print("even")
# else:
#     print("odd")

# problem"s
# 1

# a=int(input("enter the value:"))
# if(a>0):
#     print("Positive number:",a)
# elif a<0:
#     print("negative number:",a)
# else 
#       print("zero")

# 2

# a=int(input("enter the value a:"))
# b=int(input("enter the value b:"))
# c=int(input("enter the value c:"))
# if(a<b):
#     if(b<c):
#         print("c is grater number:",c)
#     else:
#         print("b is grater number:",b)
# else:
#     if(a>c):
#         print("a is grater number:",a)
#     else:
#         print("c is grater number:",c)

# 3

mark=int(input("enter the mark:"))
if(mark <= 100):
    if(mark >= 90 and mark <= 100):
        print("GRADE - A")
    elif(mark >= 75 and mark < 90):
        print("GRADE - B")
    elif(mark >= 60 and mark < 75):
        print("GRADE - C")
    elif(mark >= 40 and mark < 60):
        print("GRADE - D")
    elif(mark < 40):
        print("GRADE - F")
else:
    print("error")