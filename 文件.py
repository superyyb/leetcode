#写入
def my_write():
    file=open("a.txt","w",encoding="utf-8") #创建/打开文件
    file.write("越越今天侧方位停车停的真好！") #操作文件
    file.close() #关闭文件
#调用函数
if __name__=="__main__":
    my_write()

#读取
def my_read():
    file=open("a.txt","r",encoding="utf-8")
    s=file.read() #创建字符串s
    print(type(s),s) #type函数
    file.close()
if __name__=="__main__":
    my_read()

def my_write_list(file,lst):
    f=open(file,"a",encoding="utf-8")
    f.writelines(lst)
    f.close()
if __name__ == "__main__":
    lst=["姓名\t","年龄\t","分数\n","越越\t","18\t","100\n"]
    my_write_list("c.txt",lst)