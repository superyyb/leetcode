#用count函数
class Solution:
    def areOccurrencesEqual(s: str) -> bool:
        first_char_count = s.count(s[0])#找到字符串中第一个字符的出现次数，将其作为基准值。
        for char in set(s):  # 使用 set 去重，只检查每个字符一次
            if s.count(char) != first_char_count:
# s.count(char)：计算字符 char 在字符串 s 中出现的次数。
                return False
        return True

#字符串转换为字典映射 Counter,用set判断字典的值是否全是一个值
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
'''
例如，s = "aabbcc"，Counter(s) 的结果是 {'a': 2, 'b': 2, 'c': 2}。
Counter(s).values() 返回 [2, 2, 2]。
'''

#回顾解法：
class Solution:
    def areOccurrencesEqual(self,s: str) -> bool:
        hash={}
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        set1=set()
        for key in hash:
            set1.add(hash[key])
        return len(set1)==1
