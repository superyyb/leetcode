#抄答案前的思路：
# 想遍历这个list里每一个str，比较是否相同，
# 如果相同就存储（append）到一个list（？）里面，
# 直到比较的字母不相同为止。输出list，else输出空字符串

#c老师：
# 将数组中的第一个字符串作为参考前缀。
# 从第二个字符串开始，逐个与参考前缀进行比较。
#我的答案：
class Solution:#list=["flower","flow","fix"]
    def longestCommonPrefix(self, strs: list[str]) -> str: # 定义名为longestCommonPrefix的函数
        #list[str] 是参数类型提示，表示 strs 是一个字符串的列表。
        #-> str是函数的返回类型提示，表示该函数将返回一个字符串 (str)。
        if not strs:
            return ""
        prefix=strs[0]#参考前缀
        for str in strs[1:]:#列表切片操作
            while str[:len(prefix)]!=prefix:
                prefix=prefix[:-1]#逐渐缩短参考前缀
                if not prefix:
                    return ""
        return prefix
#创建列表
sol=Solution()
strs_1=["flower","flow","flight"]
strs_2=["dog","racecar","car"]
print(sol.longestCommonPrefix(strs_1))
print(sol.longestCommonPrefix(strs_2))

#大神答案：
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:#检查列表 strs 是否为空。如果为空，函数返回空字符串。
            return ""
        for i, letter_group in enumerate(zip(*strs)):
            """
            zip(*strs)
            使用解包操作符 * 将字符串列表strs解包，然后将每个字符串按对应位置组合成一个个元组。比如
            strs = ["flower", "flow", "flight"]，zip(*strs)会生成一个包含四个元组的序列
            [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
            当可迭代对象长度不同，zip 会以最短的可迭代对象为准，忽略多余的元素。
            用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
            
            enumerate(zip(*strs))
            为 zip(*strs) 生成的元组序列添加索引，生成 (index, letter_group) 对。
            生成 [(0, ('f', 'f', 'f')), (1, ('l', 'l', 'l')), (2, ('o', 'o', 'i')), (3,('w', 'w', 'g'))]。
            "元组套元组"
            for循环
            遍历 enumerate(zip(*strs)) 生成的索引和字符组。每次循环中，i 是索引，letter_group 是字符组。
            在第一次迭代中，i 是 0，letter_group 是 ('f', 'f', 'f')。
            """
            if len(set(letter_group)) > 1:  #set创建一个集合（无序且不重复），因此长度大于1说明有两个及以上不重复的字母
                return strs[0][:i] #字符串切片
        return min(strs)
        #防止出现所有的集合都只有一个字母的情况，永远达不到for循环的条件，因此就输出strs这个列表中长度最短的字符串，即公共前缀
sol = Solution()
strs_1 = ["flower", "flow", "flight"]
strs_2 = ["dog", "racecar", "car"]
print(sol.longestCommonPrefix(strs_1))
print(sol.longestCommonPrefix(strs_2))

#大神答案2：利用reduce
class Solution:
    def lcp(self, str1, str2):#定义一个lcp函数，找出str1和str2这两个字符串的最长公共前缀
        i = 0#初始化变量i为0用于记录当前比较的位置
        while (i < len(str1) and i < len(str2)):#限制比较次数小于字符串的长度
            if str1[i] == str2[i]:
                i = i + 1
            else:
                break
        return str1[:i] #输出这两个字符串相同的部分
    def longestCommonPrefix(self, strs):#参数strs是一个字符串列表，返回值是字符串。
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        else:
            return reduce(self.lcp, strs)
"""
strs = ["flower", "flow", "flight"] reduce开始处理，首先将strs列表的前两个元素传给lcp方法。
第一次调用lcp：lcp("flower", "flow")
比较字符：f == f(继续)  l == l(继续) o == o(继续) w == w(继续) (e != None) ，循环终止。返回结果"flow"。
第二次调用lcp：将"flow"和列表中的下一个元素"flight"传给lcp方法。lcp("flow", "flight")
比较字符：返回结果"fl"。结束：
"""