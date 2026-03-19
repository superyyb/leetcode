class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m, n = len(s), len(spaces)
        res = [' '] * (m + n)  # create the res with spaces
        j = 0
        for i, char in enumerate(s):
            if j < n and i == spaces[j]:
                j += 1
            res[i + j] = s[i]
        return "".join(res)
# 把 s 按 spaces 切成片段，用 " ".join(片段列表)

