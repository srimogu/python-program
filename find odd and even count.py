num1=int(input("enter the start number: "))
num2=int(input("enter the stop number: "))
total=0
c=0
for i in range(num1,num2+1):
    if i%2==0:
        total+=i
    else:
        c+=i
print("even number total: ",total)
print("odd number total: ",c)
