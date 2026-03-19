class Person():
    def eat(self):
        print("人吃五谷杂粮")
class Cat():
    def eat(self):
        print("猫吃猫粮")
class Turtle():
    def eat(self):
        print("龟吃龟粮")
#同名方法eat，下面开始编写函数
def fun(obj):#obj为定义的一个形参
    obj.eat()#通过对象obj调用eat方法
#创建三个对象
per=Person()
cat=Cat()
turtle=Turtle()
#调用fun函数
fun(per)
fun(cat)
fun(turtle)
