print("fsdssfd",int(3.14))
print(int(3.14),int(3.14))
print("fsdssfd "+str(int(3.14)))

a=""
print("98大于90吗？",a!=a)

print("T^T  "*20)
print("\nPython")

name="张三"
age=18*2
a,b,c,d="home"
print(a,"\n",b,"\n",c,"\n",d,"\n",name,"\n",age)

print("-"*40)
#name=input("请输入您的姓名：")
#age=input("请输入您的年龄：")
print("姓名",name)
print("年龄",age)

number=987654
print(number==987654)

n=6
if n%2:
    print(n)


import sys
while True:
    response=input("请输入exit")
    if response=="exit":
        sys.exit()
        print("You typed exit to exit.")