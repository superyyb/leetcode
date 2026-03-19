#千年虫
list1=[88,89,90,98,0,99]
list2=[]
for items in list1:
    if items==0:
        items=items+2000
    else:
        items=items+1900
    list2.append(items)
print(list2)

list1=[88,89,90,98,0,99]
lst=[]
for index in range(0,len(list1)):
    if list1[index]!=0:
        list1[index]=1900+list1[index]
    else:
        list1[index]=2000+list1[index]
print(list1)


# for i in range(1,6):
#     admin_choice=input("请输入商品编号和名称入库，每次输入一个：")
#     lst.append(admin_choice)
# #lst=["1001手机","1002华为笔记本","1003鼠标","1004薯条","1005冰淇淋"]
# print("商品有：",lst)
# user_cart=[]
# while True:
#     user_choice=input("请选择商品：")
#     if user_choice=="q":
#         user_cart.reverse()
#         print("显示购物车的物品",user_cart)
#         break
#     elif int(user_choice) in range(1001,1006):
#         user_cart.append(user_choice)
#         print("商品已成功添加入购物车")
#     else:
#         print("该商品不存在")

lst=[]
for i in range(1,6):
    admin_choice=input("请输入商品编号和名称入库，每次输入一个：")
    lst.append(admin_choice)
#lst=["1001手机","1002华为笔记本","1003鼠标","1004薯条","1005冰淇淋"]
print("商品有：",lst)
user_cart=[]
while True:
    user_choice=input("请选择商品：")
    if user_choice=="q":
        user_cart.reverse()
        print("显示购物车的物品",user_cart)
        break
    else:
        found=False #found变量用于标记是否找到了用户输入的商品编号。
        for item in lst:
            if user_choice==item[0:4]:
                user_cart.append(user_choice)
                print("商品已成功添加入购物车")
                found=True
                break
        if found==False:#或者写if not found:
            print("该商品不存在")

