student1={
    "name":"naveen",
    "age":20,
    "mark":455,
    "dept":"ECE"
}
print(student1)
print(student1["name"])
print(student1["mark"])
print(student1.get("age"))
print(student1.get("city","not aplicable"))
student1["mark"]=499
print(student1)
student1["city"]="pondy"
print(student1)
student1.pop("age")
print(student1)

for a,b in student1.items():
    print(a," :",b)

name="naveen"
dept="python"
print(name)
print(dept)
print(dept[0])
print(dept[:3])
print(dept[2:6])
print(dept[0:4])
print(dept[::-1])

a="python"
a="3"+a[1:]
print(len(a))
for ch in a:
    print(ch,end=" ")
print()
text="Java programming"
print(text.upper())
print(text.lower())