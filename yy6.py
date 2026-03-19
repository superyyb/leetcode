for i in range(1,4):
    for j in range(1,5):
        print("*",end="^")
    print()
print("-"*30)
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
print("-"*30)

for i in range(1,6):
    for j in range(1,7-i):
        print("*",end="")
    print()

print("-"*30)

for i in range(1,6):
    print(" "*(5-i)+"*"*(2*i-1))

print("-"*40)

for i in range(1,4):
    print("*"*4)

for i in range(1, 6):
    print("*"*i)



for i in range(1,6):
    print("*"*(6-i))

print("-"*30)

for i in range(1,5):
    print(" "*(4-i)+"*"*(2*i-1)+" "*(4-i))
for i in range(1,4):
    print(" "*i+"*"*(7-2*i)+" "*i)

print("-"*30)

for i in range(1,2):
    print(" "*(i+1)+"*"*i+" "*(i+1))
for i in range(2,3):
    print(" "*(i-1)+"*"*(i-1)+" "*(i-1)+"*"*(i-1))
for i in range(3,4):
    print("*"*(i-2)+" "*i+"*"*(i-2))
for i in range(2,3):
    print(" "*(i-1)+"*"*(i-1)+" "*(i-1)+"*"*(i-1))
for i in range(1,2):
    print(" "*(i+1)+"*"*i+" "*(i+1))

print("-" * 30)

for i in range(1,6):
    for j in range(1,6-i):
        print("&",end="")
    for k in range(1,i*2):
        print("*",end="")
    print()

print("-" * 30)

row=int(input("请输入菱形的行数："))
while row%2==0 or row<=0:
    row=int(input("请重新输入"))
print("菱形行数为：",row)
a=int((row+1)/2)
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1))
b=int(row//2)
for i in range(1,b+1):
    print(" "*i+"*"*(a+b-2*i))



