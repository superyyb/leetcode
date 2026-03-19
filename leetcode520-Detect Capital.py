#yy思路：一个str，要么全小写，要么全大写，要么只存在一个大写并且在第一位
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word ==word.lower() or word==word.upper() or word[0].isupper() and word[1:].islower()
sol=Solution()
print(sol.detectCapitalUse("hello"))
print(sol.detectCapitalUse("HELLO"))
print(sol.detectCapitalUse("Hello"))