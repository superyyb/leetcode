#小狗类
class Dog():
    def __init__(self,name,age):#定义三个形参，其中self为默认
        self.name=name
        self.age=age #将name，age和self关联起来
    def sit(self):
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        print(self.name.title()+" rolled over!")
My_dog=Dog("lucy",6)
your_dog=Dog("tom",1)
print("My dog",My_dog.name.title(),"is",str(My_dog.age),"years old")
print("Your dog",your_dog.name.title(),"is",str(your_dog.age),"years old")
My_dog.sit()
My_dog.roll_over()
#修改属性的值
My_dog.name="bb"
My_dog.sit()

class Student():#下一步：定义类属性和类方法
    def __init__(self,xm,nl,):#定义属性：姓名 年龄
        self.name=xm
        self.age=nl
    def show(self):#定义方法函数
        print("我叫"+self.name+"，我今年"+self.age+"岁了。")
stu1=Student("小明","14")
stu2=Student("小h","11")
stu3=Student("小e","12")
stu4=Student("小q","16")
lst=[stu1,stu2,stu3,stu4]
for item in lst:
    item.show()
#为stu2动态绑定一个属性
stu2.gender="男"
print(stu2.name,stu2.age,stu2.gender)

#为stu2动态绑定一个函数
def introduce():
    print("我是一个普通函数，我被绑定成stu2的方法")
stu2.fun=introduce #函数赋值，千万不要加()，要不然就变成调用了
stu2.fun() #为什么这里不是stu2.introduce()



