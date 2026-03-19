def visitors(names):#names是列表形参
    for name in names:
        print("Hello,",name.title(),",how are you?")
visitors_name=["tom","sarah","lily"]
visitors(visitors_name)#visitors_name是列表实参

unprinted_design=["aa","bb","cc","dd"]
printed_design=[]
while unprinted_design:#当unprinted_design不为空时退出循环
    design=unprinted_design.pop()
    print("current_design:",design)
    printed_design.append(design)
print("The following design has been printed:",printed_design)

def show_magicians(magicians):#magicians形参
    for magician in magicians:
        print(magician)
real_magicians=["qq","ww","ee","rr"]#real magicians实参
show_magicians(real_magicians)
# def make_great(magicians):
#     for i in range(len(magicians)):#返回列表 magicians 的长度，即列表中元素的个数。
#         magicians[i]+=" the Great"#将列表 magicians 中索引为 i 的元素后连the Great
#     print(magicians)
# make_great(real_magicians)
# show_magicians(real_magicians)

print("=============================")
#如何传递列表副本
def make_great(magicians):
    for i in range(len(magicians)):#返回列表 magicians 的长度，即列表中元素的个数。
        magicians[i]+=" the Great"#将列表 magicians 中索引为 i 的元素后连the Great
    print(magicians)
make_great(real_magicians[:])
show_magicians(real_magicians)#为什么把20-25行注释掉，因为20-25已经把show_magicians改为后面加the Great得了

# def making_pizza(ingredient):
#     print("Making a pizza with following ingredients:",ingredient)
# making_pizza("cheese","mushroom","pepper")
#错在哪：ingredient只接受一个参数，如果要多个参数用列表或者元组
print("=============================")

#用列表
def making_pizza(ingredients):
    for ingredient in ingredients:
        print("Making a pizza with the following ingredients:",ingredient)
real_ingredients=["cheese","mushroom","pepper"]
making_pizza(real_ingredients)

#用元组
def making_pizza(*ingredients):
    for ingredient in ingredients:
        print("Making a pizza with the following ingredients:",ingredient)
real_ingredients=("potato","beef","pork")
making_pizza(real_ingredients)

print("----------------元组加位置实参------------------")
#结合使用位置实参和任意数量实参
def make_pizza(size,*ingredients):
    print("Making a pizza in",str(size),"inch within the following ingredients:")
    #先书写size的函数用法，再遍历函数中的元组
    for ingredient in ingredients:
        print(ingredient)
make_pizza(16,"mushroom","peppper","beef")
make_pizza(12,"pork","cheese")

print("----------------列表加位置实参------------------")
def make_pizza(size,ingredients):
    print("Making a pizza in",str(size),"inch within the following ingredients:")
    #先书写size的函数用法，再遍历函数中的元组
    for ingredient in ingredients:
        print(ingredient)
make_pizza(16,["mushroom","peppper","beef"])
make_pizza(12,["pork","cheese"])

def build_profile(first,last,**user_info):
    profile={"first_name":first,"last_name":last}
    for key,value in user_info.items():
        user_info={key:value}
    return build_profile()
p=build_profile("tom","ford","age"=10,"favorite_color"="blue")
print(p)