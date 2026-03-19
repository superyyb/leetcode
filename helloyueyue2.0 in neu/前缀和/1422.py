class Solution:
    def maxScore(self, s: str) -> int:
        #left zeros + right ones
        max_score = 0
        count_zero = 0
        count_one = 0
        for i in range(len(s)):
            if s[i] == "1":
                count_one += 1
        for i in range(len(s) - 1): #保证右边至少有一个字符
            if s[i] == "0":
                count_zero += 1
            else:
                count_one -= 1
            max_score = max(max_score, count_one + count_zero)
        return max_score
