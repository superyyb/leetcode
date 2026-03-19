#zip函数逐个比较
class Solution:
    def isIsomorphic1(self, s: str, t: str) -> bool:
        word = zip(*set(zip(s, t)))
        for w in word:
            if len(w) != len(set(w)):
                return False
        return True


#yy思路：s进哈希表，t
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1=dict()
        dic2=dict()
        for i in range(len(s)):
            z



        if len(s)!=len(t):
            return False
