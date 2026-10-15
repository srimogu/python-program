a=int(input("enter the number: "))
b=1
for i in range(1,a+1):
    b=b*i
    print(i,end=" ")
    if i<a:
        print("*",end=" ")
print("=",b)
print("factorial of ",a,": ",b)
