a=float(input("enter the amount:"))
dis=0.0
#d=a*per/100
if(a<0):
    print("invalid amout")
else:
    if a>= 5000:
        dis=a*20/100
        print("DISCOUNT:20%")
    elif a>=2000 and a<5000:
        dis=a*10/100
        print("DISCOUNT:10%")
    print("discounted amount: ",dis)
    print("final amount: ",a-dis)