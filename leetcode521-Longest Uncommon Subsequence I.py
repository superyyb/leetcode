#yy思路：本来想用find的，但是c老师说
# find 用于查找子串的位置，而不是用来判断两个字符串是否相等或哪个更长
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:#判断a，b字符串是否相等
            return -1
        else:
            return max(len(a), len(b))    #返回最长的字符长度

        # for i,j in a,b:
        #     if a[i]==b[j]:

