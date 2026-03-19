# apple_num=0
# while True:
#     apple=input("越越今天吃了苹果吗？")
#     if apple=="Y":
#         apple_num+=1
#     if apple=="N":
#         break
# print("越越今天吃了"+str(apple_num)+"个苹果")

apple_num=0
i=True
while i:
    apple=input("越越今天吃了苹果吗？输入Y/N回答")

    if apple=="Y":
        apple_num+=1
    elif apple=="N":
        i=False
    else:
        i = True
        print("请输入正确符号！")
print("越越今天吃了"+str(apple_num)+"个苹果")