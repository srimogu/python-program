lint1=[12,13,12,23,34,45]
lint2=['java','c','c++',23,2.3,True]
print(lint1)
print(lint2)
print(type(lint2))
list1=[12,32,43,3]
list1[2]=300
print(list1)

numbers=[]
n=int(input())
for i in range(n):
    data=int(input())
    numbers.append(data)
print(numbers)

for data in lint1:
    print(data,end=" ")
print()
i=0 
while i<len(lint1):
    print(lint1[i],end=" ")
    i+=1
print()

list6=[1,2,3,4,5]
list6.append(6)
list6.append(7)
print(list6)
list6.insert(0,1000)
print(list6)

list7=[10,20,30,40,20,30]
list7.remove(30)
print(list7)
list7.pop()
print(list7)
list7.clear()
print(list7)

print("Index")
list7=[1,2,3,4,5]
print(list7[4])
print(list7[-4])

num=[10,20,30,40,50,60,70]

print(num[1:4])
print(num[:4])
print(num[2:])
print(num[::4])
print(num[-3:])
print(num[::-1])
print(num[:])

num1=[10,20,30,40]
print(10 in num1)
print(num1.count(10))
print(num1.index(30))

num=[23,34,45,56,67,0,-9]
num.sort()
print(num)
num.sort(reverse=True)
print(num)

num1=[2,3,4,5]
num1.reverse()
print(num1)

num=[1,2,34,32,5,42,5,3,654,75,3,98,76,54,33,55,78,9,54,78,22]
print(len(num))
print(sum(num))
print(min(num))
print(max(num))