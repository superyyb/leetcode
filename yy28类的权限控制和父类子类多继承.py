class Student():
    def __init__(self,name,age,gender):
        self._name=name #只能子类和本身访问
        self.__age=age #只能类本身访问
        self.gender=gender #不限制访问
    def _fun1(self):
        print("子类及本身访问")
    def __fun2(self):
        print("只能本身访问")
    def fun3(self):
        print("普通实例方法")

#调用属性
stu=Student("OMING",20,"女")
print(stu.gender)
print(stu._name)
#print(stu.__gender) 无法运行

#调用方法
stu._fun1()
stu.fun3()

#如何调用私有方法和属性
print(stu._Student__age)
stu._Student__fun2()

#子类
class Person:#默认继承了object
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("大家好，我是",self.name,"我的年龄是",self.age)
per=Person("xiaoming",26)

class Student(Person):#作为person子类的标志
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    # def show(self):
    #     print(self.subject)
class Doctor(Person):
    def __init__(self,name,age,work):
#调用父类中的方法
        super().__init__(name,age)
        self.work=work

#创建子类对象
stu=Student("CYY",18,"English")
doc=Doctor("PYY",18,"surgen")

#多继承
class FatherA():
    def __init__(self,name):
        self.name=name
    def showA(self):
        print("调用父类A的方法，我叫",self.name)
class FatherB():
    def __init__(self,age):
        self.age=age
    def showB(self):
        print("调用父类B中的方法，我今年",self.age,"岁了")
class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
#如何调用两个father中的初始化方法
#不能再用super().了，而是要用父类名称区分
        FatherA.__init__(self,name)
        FatherB.__init__(self,age)
#给自己的实例属性关联self
        self.gender=gender
#-----------以上为初始化方法，接下来设置参数-------------------
son=Son("xiaohong",15,"female")
son.showA()
son.showB()