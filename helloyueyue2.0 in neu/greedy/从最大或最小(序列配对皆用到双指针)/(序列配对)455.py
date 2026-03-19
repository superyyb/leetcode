class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #双指针双序列
        i, j = 0, 0
        count = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                count += 1
            j += 1
        return count

#少写一个count 直接用i计数
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #双指针双序列
        i, j = 0, 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i