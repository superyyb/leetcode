for i in "dictionary":
    if i=="o":
        break
    print(i)

s=0
i=20
while i<=100:
    if i%2==1:
        i=i+1
        continue
    s=s+i
    i=i+1
print(s)

year=int(input("请输入年份："))
if year%4==0 and year%100!=0:
    print(year,"年为闰年")
else:print(year,"年为平年")

print("欢迎进入10086自助查询系统！")
number=int(input("请输入1-3的数字查询相关信息"))
while number==1:
    print("您当前余额为：")


if number==1:
    print("您当前余额为：")
if number==2:
    print("您当前流量为：")
if number==3:
    print("您当前剩余通话为：")
if number==0:
    print("退出自助查询系统")
