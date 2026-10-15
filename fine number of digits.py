n=int(input("enter the number:"))
digits=0
total=0
rem=0
while n!=0:
    rem=n%10
    digits+=1
    #print(digits)
    total=total+rem
    n=n//10
print("no of digits:",digits)
print("sum of digits:",total)