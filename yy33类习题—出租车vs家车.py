class car():#父类
    def __init__(self,type,number):
        self.type=type
        self.number=number
    def start(self):
        print("我是车，我能启动")
    def stop(self):
        print("我是车，我能停止")
class taxi(car):
    #记得子类定义的时候括弧里写父类名称！！！
    def __init__(self,type,number,company):
        super().__init__(type,number)
        self.company=company#定义新的属性
    #重写父类的方法
    def start(self):
        #也可以用：print(f"乘客您好！我是{self.company}的")
        print("乘客您好！我是",self.company,"的，我的车牌是",self.number,"您要去哪里？")
    def stop(self):
        print("目的地到了，请您付款下车。")
class homecar(car):
    def __init__(self,type,number,owner_name):
        super().__init__(type,number)
        self.owner_name=owner_name
    def start(self):
        print("我是cyy，我的小蓝我做主")
    def stop(self):
        print("目的地到了，小蓝一边呆着去吧")
#定义函数
def use(car):
    car.start()
    car.stop()
#创建car实例
car_A=taxi("ZEEKR","苏D533PN","AAA")
car_B=homecar("BYD","苏D09A59","CYY")
#运行
use(car_A)
use(car_B)

# 或者直接写
# car_A=taxi("ZEEKR","苏D533PN","AAA")
# car_A.start()
# car_A.stop()