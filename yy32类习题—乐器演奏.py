class Instrument():
    def make_sound(self):
        pass
class Erhu(Instrument):
    def make_sound(self):
        print("二胡在演奏")#重写父类方法
class Piano(Instrument):
    def make_sound(self):
        print("钢琴在演奏")
class Pipa(Instrument):
    def make_sound(self):
        print("琵琶在演奏")
        #以上是定义三种不同乐器的类，不是在定义播放函数
        # 需要单独定义一个函数，这个函数接受一个乐器对象作为参数，
        # 并调用该乐器对象的 make_sound 方法，以实现播放不同乐器的功能。
        # 这就是为什么后面还需要定义一个函数 play 的原因。
#定义一个播放函数
def play(instrument):
    instrument.make_sound()
#创建乐器实例
Er=Erhu()
Pi=Piano()
Pa=Pipa()
#运行
play(Er)
play(Pi)
play(Pi)


