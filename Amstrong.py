num=int(input())
digit=0
temp=num
while(num!=0):
    num//=10
    digit+=1
sum=0
num=temp
while(temp!=0):
    rem=temp%10
    temp=temp//10
    sum=sum + rem**digit
if(num==sum):
    print("it's amstrong number: ",num,"=",sum)
else:
    print("not amstrong number: ",num,"=",sum)