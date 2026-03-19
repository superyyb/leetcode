apple_num=0
i=True

while i:
    apple=input("越越今天吃了苹果吗？")
    if apple=="Y":
        apple_num+=1
    else:
        i=False

print("越越今天吃了"+str(apple_num)+"个苹果")