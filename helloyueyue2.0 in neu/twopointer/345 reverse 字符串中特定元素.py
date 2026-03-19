class Solution:
    def reverseVowels(self, s: str) -> str:#[123a42o3]
        i, j = 0, len(s) - 1
        vowels = set("aeiouAEIOU")
        s = list(s)
        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
#为什么要把s先转为list再转回string：
# 字符串是不可变对象