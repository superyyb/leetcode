#yy思路：
# 将str转为list 创建指针 if i in magazine：return True
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote=list(ransomNote) #为什么写成list(r)会报错啊
        magazine=list(magazine)
        n=len(ransomNote)
        i=0
        while i<n:
            if ransomNote[i] in magazine:
                i+=1 #如果在magazine里，指针朝后移动
                return True
            else:
                return False
        错误：无法实现only appear for once
"""
#解法1：Counter()函数
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for char in ransom_count:#char表示ransom_count这个字典中所有的key（即元素）
            if ransom_count[char] > magazine_count[char]:#dict[key] = value
                return False
        return True
sol=Solution()
print(sol.canConstruct("a","b"))
print(sol.canConstruct("aa","ab"))
print(sol.canConstruct("aa","aab"))

#解法2：集合 ？？？？？？？？？？？？
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1, st2 = Counter(ransomNote), Counter(magazine)
        if st1 & st2 == st1:
# Counter 对象的交集
# 返回一个新的 Counter 对象，其中每个键的值是 st1 和 st2 中对应键的较小值（即交集）。
#检查 st1 是否是 st2 的子集。
# 如果 st1 中每个字符的出现次数都小于或等于 st2 中的对应字符出现次数，
# 则 st1 & st2 等于 st1，即 st1 是 st2 的子集。
            return True
        return False

#解法3：replace()
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = True #初始化结果为True
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char,'',1)
# 如果在 magazine 中找到了字符 char，则从 magazine 中移除一个 char
            else:
                result = False
                break
# 如果在 magazine 中找不到字符 char，则无法构造成功，将 result 设置为 False，并跳出循环
        return result