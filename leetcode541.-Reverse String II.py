    '''
#yy思路：str切片，但是由于每种情况不一样，要考虑到字符串长度n和k之间的关系式
#2k个字符中前k个反转即：以k为模块中字符数量，每个模块相间隔1，3，5个模块反转，2，4，6不动
#如果剩下的（即余数 n%2k）<k，则全部反转

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
s[]
#双指针法？s[i]和s[j]互换？
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #要想修改字符：先把str改为list
        s=list(s)
        n=len(s)
        if 2*k>n:
            s=reversed(s)
        if 2*k<n:
            for i in range(0,n,2*k):
                for j in range(0,n,2*k+1):
                    s[i:j]=reversed(s[i:j])
                # s[i],s[j]=s[j],s[i]#前提是步长为2才可以这么写
                i+=2*k
                j+=2*k+1
                if n%(2*k)<k:
                    s[-n%(2*k):]=s[-n%(2*k):].reverse()
        return ''.join(s)
    '''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 将字符串转换为列表，以便修改字符
        s = list(s)
        n = len(s)

        # 遍历每2k字符的块
        for i in range(0, n, 2 * k):
            # 反转前k个字符
            # 计算当前块的结束位置
            end = min(i + k, n)
            s[i:end] = reversed(s[i:end])
#根本不需要用余数，步长为2k已经限制了剩下的不超过2k，且min(i+k,n)限制了不超过k
        # 将列表转换回字符串
        return ''.join(s)

#解法二：切片拼凑
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0 #初始化i
        while i < len(s):
            s = s[:i]+s[i:i+k][::-1]+s[i+k:]
            # s[:i]：字符串的前一部分，不变。
            # s[i:i + k][::-1]：取出从位置i开始的长度为k的子字符串，并进行反转。
            # s[i + k:] 从位置 i + k开始到字符串结尾的部分，不变。
            # 将三部分拼接起来，生成新的字符串，替换原来的字符串s。
        return s
    #岂不是s的值每一次while循环都需要更新一遍，是不是有点复杂了，不能一步到位到最后一次循环么，
    #有点搞不明白s是每次更新还是每次叠加