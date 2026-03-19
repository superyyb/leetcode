class Solution:
    def countSubstrings(self, s: str) -> int:
        #backtracking
        n = len(s)
        count = 0
        def isPalindromic(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def backtracking(start):
            nonlocal count
            if start == n:
                return
            for end in range(start, n):
                if isPalindromic(start, end):
                    count += 1
            backtracking(start + 1)
        backtracking(0)
        return count