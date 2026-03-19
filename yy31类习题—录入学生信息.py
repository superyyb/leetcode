class Student():
    def __init__(self,xm,nl,xb,fs):
        self.name=xm
        self.age=nl
        self.gender=xb
        self.grade=fs
    def info(self):
        print(self.name,self.age,self.gender,self.grade)
print("请输入5位学生信息：姓名#年龄#性别#成绩")
lst=[]#用于存储五个学生对象
for i in range(1,6):
    s=input(f"请输入第{i}位学生信息及成绩：") #好神奇
    s_lst=s.split("#") #为什么这里要写s_lst而不能直接把s加进列表里
    stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])#也不能理解
    lst.append(stu)
#遍历列表，调用info方法
for item in lst:
    item.info()