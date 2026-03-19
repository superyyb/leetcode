#确保网站每一位用户用户名独一无二
current_users=["a","b","c","d","e"]
new_users=["a","f","h","j","d","z"]
name=input("新注册用户请输入用户名：")
#for user in new_users:
if name in current_users or name in new_users:
    print("该用户名已存在！请输入其他用户名:")
else:
    print("该用户名未被使用")

#确保网站每一位用户用户名独一无二
current_users=["a","b","c","d","e"]
new_users=["a","f","h","j","d","z"]
name=input("请输入新注册用户名：")
for user in new_users:#就算我输入一个不在new_users列表里的name，也不要紧啊，这句话有什么意义
    if name in current_users:
       print("该用户名已存在！请输入其他用户名:")
       break
    else:
        print("该用户名未被使用")
        break

#确保网站每一位用户用户名独一无二
current_users=["a","b","c","d","e"]
new_users=["a","f","h","j","d","z"]
while True:
    name=input("请输入新注册用户名：")
    if name in current_users:
        print("该用户名已存在！请输入其他用户名:")
    else:
        print("该用户名未被使用")
        break
#疑问：既然name需要用户输入，那要new_users这个列表干嘛

#5-11序数
#number=[1,10] 怎么能这么蠢呢？？？
#number=(1,10)
for num in range(1,10):
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")

current_users=["a","b","c","d","e"]
new_users=["a","f","h","j","d","z"]
for user in new_users:
    if user in current_users:
        print(user,"用户名已存在！")
    else:
        print(user,"用户名不存在")
