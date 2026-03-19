"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list_m=[]
        list_n = []
        for m in magazine:
            list_m.append(m)
        for n in ransomNote:
            list_n.append(n)
        print(list_m)
        for m in list_m:
            if m in list_n:
                list_n.remove(m)
        return list_n==[]
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash={}
        for r in ransomNote:
            if r in hash:
                hash[r]+=1
            else:
                hash[r]=1
        for m in magazine:
            if m in hash:
                hash[m]-=1
                if hash[m]==0:#如果已经删到了最后一个m 直接把m从哈希表中删除
                    del hash[m]
        return hash=={}

sol=Solution()
print(sol.canConstruct(ransomNote = "aa", magazine = "aab"))

