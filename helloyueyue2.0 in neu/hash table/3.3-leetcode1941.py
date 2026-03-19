class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hash={}
        for item in s:
            if item in hash:
                hash[item]+=1
            else:
                hash[item]=1
        set1=set()
        for key in hash:
            set1.add(hash[key])
        return len(set1)==1

sol=Solution()
print(sol.areOccurrencesEqual("abcbkkc"))