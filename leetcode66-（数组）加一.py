#yy思路：数字加一：暴力一点，列表转int再转列表
# 分两种情况，末位数小于9：直接加一
# 末位数为9，
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        str_1="".join(map(str,digits)) #join只能接字符串列表，要先把整数转为字符串
        int_1=int(str_1)
        int_2=int_1+1
        str_2=str(int_2)
        list_1=list(map(int,str_2)) #将字符串每个字符转为单个字符串再转为整数
        #"123"转为“1”“2”“3”  为什么不能用list_1=str_2.split()
        return list_1
        #为什么一定要用map呢，用append把int一个一个添加到list里也可以啊，如下
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''
        l = []
        for i in digits:
            s = s + str(i)  # 全部转换成字符串
        for n in str(int(s) + 1):  # 字符串转换成int类型然后+1，再遍历字符串 添加到数组
            l.append(int(n))
        return l


        # i=len(digits)
        # if digits[i-1]<9:
        #     digits[i-1]+=1
        # else:
        #     digits.pop(i-1)
        #     digits.append(1)
        #     digits.append(0)
        # return digits
if __name__=="__main__":
    sol=Solution()
    lst=[4,3,2,1]
    lst2=[9,9]
    print(sol.plusOne(lst))
    print(sol.plusOne(lst2))