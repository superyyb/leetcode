class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Initially, we assume nothing is a palindrome (False)
        dp = [[False] * n for _ in range(n)]
        left = 0
        max_len = 1
        #Traversal Order: Bottom to top (i), Left to right (j)
        for i in range(n - 1, -1, -1):
            for j in range(i, n):#j must be bigger than i
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    left = i
        return s[left : left + max_len]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Memoization: In recursion, same parameters may appear more than once, so we use memoization to avoid unnecessary spaces
        '''
        1.Define isPalindrome(i,j) as str[i: j+1] is palindrome
        def isPalindrome(i,j)(i, j):
            if i >= j:
                return True
            if memo[i][j]:
                return memo[i][j]
            #same i, j appear before, just return previous result(memo[i][j])
            res = (s[i] == s[j]) and isPalindrome(i+1, j-1)
            memo[i][j] = res
            return res
        从中间往两头扩。j:1->n  i:j-1->-1
        '''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        best = f'{s[0]}'
        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    if i + 1 == j or dp[i + 1][j - 1]:#如果到头了或者中间是回文
                        dp[i][j] = True
                    if len(best) < j - i + 1:
                        best = s[i:j + 1]
        return best