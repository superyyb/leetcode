class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        freq = {}
        flag = False
        for char in s:
            freq[char] = freq.get(char, 0) + 1#treat upper and lower as two diff chars
        for value in freq.values():
            if value % 2 == 0: #even
                count += value
            if value % 2 != 0: #odd
                count += value - 1 #"ccc"we can only use the biggest odd part
                flag = True
        return count + 1 if flag == True else count
