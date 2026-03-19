class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        n = len(s)
        count = 0
        max_ans = ans = 0
        for right in range(n):
            if right >= 1 and s[right] == s[right - 1]:
                count += 1
            while count > 1 and left <= right:
                if s[left] == s[left+1]:#缩的时候注意判断条件count是否改变
                    count -= 1
                left += 1
            ans = right - left + 1
            max_ans = max(max_ans, ans)
        return max_ans

        """
        不可以写成for right in range(n-1):
            if s[right] == s[right + 1]:这样会漏掉最后一个字符
        """