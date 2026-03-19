print("你好"+" 这是一句代码"+" 哈哈")

print("let's go")
print('let\'s go')
print('\n')
print("我是第一行\n我是第二行")
print("""夏季，是一年四季中第二个季节，
炙热的阳光，滚烫的空气，树下乘凉的老人，嬉戏玩闹的孩子，
每个人脸上的笑容，生如夏花般在这个季节绽放。
《生如夏花》出自印度诗人泰戈尔《飞鸟集》第82首。
英文原文是:\"Let life be beautiful like summer flowers And Death like autumn leaves.\" 
仅此一句。译为“生如夏花之绚烂，死如秋叶之静美”。
诗歌语言清丽，意味隽永，将抒情和哲思完美结合，给人以无尽美感和启迪。""")

print("您好，吃了吗"+" 张三")
greet="您好，吃了吗"
print(greet+" 李四")
greet_Chinese=greet
greet_English="Yo What's up"
print(greet_English+" 李四")
greet=greet_English
print(greet+" SC")

a=-1
b=-2
c=3
result1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
result2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
print(result1)
print(result2)

#练习求字符串长度
print(len("Hello,world!"))
s="yy和sc"
print(len(s))

#练习通过索引获取单个字符
print(s[2])

#布尔类型
b1=True
b2=False

#空值类型
b3=None

#type函数
print(type(s))
print(type(b3))
print(type(1))

print(42!="42")

name=input()
if name=="Alice":
    print("Hi,Alice!")
else:
    print("Hi,stranger!")

name=input("请输入名字")
age=int(input("请输入年龄"))
if name=="Alice":
    print("Hi,Alice!")
elif age<12:
    print("You are not Alice,kid")
elif age>20:
    print("unlike you ,Alice is still a child")

spam=0
while spam<5:
    print("Hello,world!")
    spam=spam+1

name="1"
while name!="your name":
    print("Please type your name.")
    name=input()
print("Thank you")

while True:
    user_input=input("请输入quit退出循环")
    if user_input=="quit":
        break#当用户输入quit时退出循环
    else:
        print("你输入了："+user_input)