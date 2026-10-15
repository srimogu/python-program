tuple1 = (34,67,89,23)
print(tuple1)
print(type(tuple1))

tuple2=(5,)
print(type(tuple2))

tuple3 = (12,34,45,56,67)
for data in tuple3:
    print(data,end=" ")
print()
i=0
while i<len(tuple3):
    print(tuple3[i],end=" ")
    i+=1
print()

tuple4=(1,2,3,4,5,6)
print(tuple4.count(4))
print(tuple4.index(4))

print(len(tuple4))
print(sum(tuple4))
print(min(tuple4))
print(max(tuple4))