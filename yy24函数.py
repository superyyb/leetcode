def greet_users(name):#name要求为字符串形式
    print("Hello",name,"!")
greet_users("yueyue")

def display_message():
    print("本章学的是函数")
display_message()

def favorite_book(book_name):
    print("My favorite book is",book_name)
favorite_book("Alice in Wonderland")

def describe_pet(pet_type,pet_name):
    print("I have a",pet_type)
    print("My",pet_type,"is",pet_name.title())
describe_pet("turtle","xiaolv")
describe_pet("turtle","xiaohong")
describe_pet(pet_name="puding",pet_type="doggie")

#默认值
def describe_pet(pet_name,pet_type="dog"):
    print("I have a",pet_type)
    print("My",pet_type,"is",pet_name.title())
describe_pet("xiaobai")#实参没有指定的时候，默认从第一个开始排列，所以第20行先写name，再写指定了为dog的type
#在使用默认值的时候，形参列表中必须先列出没有默认值的形参，再列出有默认值的形参

def get_name(first_name,last_name):
    full_name=first_name+" "+last_name
    return full_name
musican=get_name("yue","chen")
print(musican)

def get_name(first_name,last_name,middle_name=""):
    if middle_name:
        full_name=(first_name,middle_name,last_name)
    else:
        full_name = (first_name, last_name)
    return full_name#为什么加不了.title()
person_name=get_name("jimmy","chou",'WW')
print(person_name)

def build_person(first_name,last_name,age=""):
    person={"first":first_name,"last":last_name}
    if age:
        person["age"]=age#将 age作为键添加到 person 字典中，并将提供的年龄值与键 "age" 关联起来。
    return person
musican=build_person("Jimmy","Zhou",age=22)
print(musican)

# def user_name(first_name,last_name):
#     full_name=first_name+" "+last_name
#     #这叫放在一个元组里，函数会返回元组的full_name=(first_name, last_name)
#     return full_name
# while True:
#     first_name=input("请输入您的姓氏：")
#     last_name=input("请输入您的名字：")
#     full_name=user_name(first_name,last_name)#为什么一定要加这句啊
#     print("Hello!",full_name)

def user_name(first_name,last_name):
    full_name=first_name+" "+last_name
    #这叫放在一个元组里，函数会返回元组的full_name=(first_name, last_name)
    return full_name
while True:
    first_name=input("请输入您的姓氏：")
    if first_name == "quit":
        break
    else:
        continue
    last_name=input("请输入您的名字：")
    full_name=user_name(first_name,last_name)#为什么一定要加这句啊
    # if first_name=="quit":
    #     break
    # if last_name=="quit":
    #     break
    print("Hello!",full_name)




