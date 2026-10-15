num=[]
sum=0
n=int(input("enter the number: "))
for i in range(n):
    data=int(input("value: "))
    num.append(data)
print("")
target=int(input("target value: "))
for i in range(n):
    for j in range(i+1,n):
        if num[i]+num[j]==target:
            sum=num[i]+num[j]
            print("target: ",target,"-",sum)
            print("list value: [",num[i],"]-[",num[j],"]")
            print("index value:[",i,"][",j,"]")
            print("")