class Circle():
    def __init__(self,r):
        self.r=r
    def get_area(self):
        print("计算圆的面积S为",3.14*self.r**2)
        #还有一种方法是return 3.14*self.r**2
        #注意代入函数用法的是self.r，不是r！！！！！
    def get_perimeter(self):
        print("计算圆的周长为",3.14*2*self.r)
radius=Circle(3)
radius.get_area()
radius.get_perimeter()

#老师的答案：
class Circle:
    def __init__(self,r):
        self.r=r
    def get_area(self):
        return 3.14*self.r**2
    def get_perimeter(self):
        return 3.14*2*self.r
#创建对象
r=eval(input("请输入圆的半径："))
#int和str相互转换！！！
radius=Circle(r)
#调用方法
area=radius.get_area()
perimeter=radius.get_perimeter()
print("圆的面积为：",area)
print("圆的周长为",perimeter)