#思路：构建hash，遍历s，hash[key]+=1,遍历t，hash[key]-=1,为0，delete
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash={}
        for s_item in s:
            if s_item in hash:
                hash[s_item]+=1
            else:
                hash[s_item]=1
        for t_item in t:
            if t_item not in hash:
                return False
            else:
                hash[t_item]-=1
            if hash[t_item]==0:
                del hash[t_item]
        return len(hash)==0#or return hash=={}

#9.8重做
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):#和下面的条件二选一
            return False
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        for char in t: #其实应该是写if t_item not in hash: return False，保证t里没有多余的元素
            if char in seen:
                seen[char] -= 1
                if seen[char] == 0:
                    del seen[char]
        return len(seen) == 0

if __name__=="__main__":
    sol=Solution()
    print(sol.isAnagram(s = "ab", t = "a"))
