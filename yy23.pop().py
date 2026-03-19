unconfirmed_user=["Alice","Bob","Clare"]
confirmed_user=[]
while unconfirmed_user:
    current_user=unconfirmed_user.pop()
    confirmed_user.append(current_user)
for user in confirmed_user:
    print(user)

response={}
active=True
while active:
    name=input("请输入名字：")
    answer=input("请输入你喜欢的食物：")
    response[name]=answer#将输入内容一一对应存入字典
    repeat=input("还有其他答案吗？Yes/No")
    if repeat=="No":
        active=False
print(name,"'s favorite food is",answer)