#yy思路：b中字符不仅要在a中出现，并且出现次数要大于a的出现次数
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countA=Counter(ransomNote)
        countB=Counter(magazine)
        for num,count in countA.items():
            if num not in countB or count>countB[num]:
                return False
        return True

#先把错误条件放前面，要不然只要有一个字母符合，就判断True了
'''
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countA=Counter(ransomNote)
        countB=Counter(magazine)
        for num,count in countA.items():
            if num in countB and count<=countB[num]:
                return True
        return False
'''

#解法2：移除字母直至为0
'''
for 循环遍历 magazine 的列表 m ，如果 m 中有字母在 ransomNote 的列表 r 中，
代表 ransomNote 中该字符能由 magazine 里面的字符构成，则将列表r中的该字母去除。
最后判断 ransomNote 列表的长度，如果为 0，返回 True，反之不行，返回 False
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = list(magazine)
        r = list(ransomNote)
        for i in range(0, len(m)):
            if m[i] in r:
                r.remove(m[i])
        if len(r) == 0:#简化为return len(r)==0
            return True
        else:
            return False

#回顾解法：
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash={}
        for i in ransomNote:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for j in magazine:
            if j in hash:
                hash[j]-=1
                if hash[j]==0:
                    del hash[j]
        if not hash:
            return True
        return False
