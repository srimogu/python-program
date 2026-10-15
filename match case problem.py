#match case problem

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
opeator=input("enter the operator: ")
match opeator:
    case'+':print(num1+num2)
    case'-':print(num1-num2)
    case'*':print(num1*num2)
    case'/':print(num1/num2)
    case'//':print(num1//num2)
    case'%':print(num1%num2)
    case'**':print(num1**num2)


file=input("enter the file name: ")
match file:
    case'py':print("python file")
    case'c':print("C file")
    case'c++':print("C++ file")
    case'html':print("HTML file")
    case'jpg':print("Image file")
    case _:print("Unknow file type")