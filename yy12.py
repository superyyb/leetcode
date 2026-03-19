import random
rand=random.randint(1,100)
#i为用户输入次数
for i in range(1,4):
    user_response=int(input("请输入1-100之间的整数："))
    if user_response>rand:
        print("大了")
    elif user_response<rand:
        print("小了")
    elif user_response==rand:
        print("正确")
    else:
        break
print("请24小时后重试")

print("-"*40)

import random
rand=random.randint(1,100)
#i为用户输入次数
i=1
while i<=10:
    user_response = int(input("请输入1-100之间的整数："))
    if user_response>rand:
        print("大了")
    elif user_response<rand:
        print("小了")
    else:
        print("正确")
        break
    i=i+1
if i<=3:
    print("你真聪明，一共猜了",i,"次。")
if 3<i<=6:
    print("还可以，一共猜了", i, "次。")
if i>6:
    print("有点菜哦，一共猜了", i, "次。")