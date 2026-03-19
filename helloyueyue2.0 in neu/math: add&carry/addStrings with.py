class Solution:
    def addDecimals(self, num1: str, num2: str) -> str:
        i, j = 0, 0
        m = len(num1)
        n = len(num2)
        integer1 = ''
        integer2 = ''
        while i < m or j < n:
            if num1[i] != '.':
                integer1 += num1[i]
                i += 1
            if num2[j] != '.':
                integer2 += nums2[i]
                j += 1
        def addStrings(a, b):
            if a
