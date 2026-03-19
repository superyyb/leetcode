class Solution:

    def encode(self, strs: List[str]) -> str:
    #["neet","code","love","you"]->"4#neet4#code4#love3#you"
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:#双指针交替
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":#为什么不能用if，有可能是12#neet，需要越过所有数字找到#
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res