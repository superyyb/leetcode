class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s={}
        hash_t={}
        for i in range(len(s)):
            if s[i] in hash_s and hash_s[s[i]]!=t[i]:
                return False
            if t[i] in hash_t and hash_t[t[i]]!=s[i]:
                return False
            hash_s[s[i]]=t[i]#构建s和t的映射关系 hash_s={"b":"f"},hash_t={"f":"b"}
            hash_t[t[i]]=s[i]
        return True

if __name__=="__main__":
    sol=Solution()
    print(sol.isIsomorphic(s = "bar", t = "foo"))
