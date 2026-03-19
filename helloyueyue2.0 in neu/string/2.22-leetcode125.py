class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():#⚠️必须要加 i < j 判断
    #如果 s[i] 一直不是字母数字，i 会无限往后加，可能超过 j，触发 IndexError。
                i += 1
            while i < j and not s[j].isalnum():#⚠️必须要加 i < j 判断
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

sol=Solution()
s="A man, a plan, a canal: Panama"
result=sol.isPalindrome(s)
print(result)
