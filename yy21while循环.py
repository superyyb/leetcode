#用户键入quit退出循环
prompt="Tell me sth., I will repeat it to you."
prompt+="\nprint 'quit' to end the program."
message=""
while message!="quit":
    message=input(prompt)
    print(message)

#改进版 嵌套
prompt="Tell me sth., I will repeat it to you."
prompt+="\nprint 'quit' to end the program."
message=""
while message!="quit":
    message=input(prompt)
    if message!="quit":
        print(message)

#改进版 True作为标志
prompt="Tell me sth., I will repeat it to you."
prompt+="\nprint 'quit' to end the program."
message=""
i=True
while i:
    message=input(prompt)
    if message=="quit":
        i=False
    else:
        print(message)

#改进版 break代表quit退出
prompt="Tell me sth., I will repeat it to you."
prompt+="\nprint 'quit' to end the program."

while True:
    message=input(prompt)
    if message=="quit":
        break
    else:
        print(message)