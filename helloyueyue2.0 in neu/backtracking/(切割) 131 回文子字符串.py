#另写函数判断是否回文 更加清晰
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
        path = []
        def isPalindrome(s, i, j):#双指针判断是否回文
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def backtracking(startIndex):
            if startIndex == len(s): #base case是难点:当index到末尾时，形成完整的path
                res.append(path[:])
                return
            for i in range(startIndex, len(s)):
                if isPalindrome(s, startIndex, i):
                    path.append(s[startIndex : i + 1])#当前判断的回文子串
                    backtracking(i + 1)
                    path.pop()
        backtracking(0)
        return res