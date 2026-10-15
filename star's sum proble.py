for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")

n=5
for i in range(1,n+1):
    print("",end=" ")
    for j in range(1,i+1):
        if j!=1 and i!=1:
            print("",end="")
        print(i,end=" ")
    print(" ")

n=5
a=n-1
b=1
for i in range(1,n*2):
    for j in range(1,a+1):
        print(" ",end=" ")
    for k in range(1,b+1):
        print("*",end=" ")
    print()
    if i>=5:
        a+=1
        b-=2
    else:
        a-=1
        b+=2
