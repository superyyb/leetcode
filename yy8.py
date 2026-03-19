s=0#存储累加和
i=0
while i<11:
    s=s+i
    if s>20:
        break
    i=i+1
    print("当前累加和的i值为；",i,"当前累加和s为：",s)

i=1#i为用户登录次数
while i<=3:
    user_name=input("请输入用户名:")
    password=input("请输入密码：")
    if user_name=="yy" and password=="yyds":
        print("欢迎进入！")
        break
    else:
        if i<=2:
            print("密码错误，您还有",3-i,"次机会")
    i=i+1
else:
    print("请于三个工作日后申请解冻账号！")


