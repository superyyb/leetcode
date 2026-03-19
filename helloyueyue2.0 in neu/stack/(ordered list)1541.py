class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0  # 插入次数
        need = 0  # 需要多少个 ')' 来把前面的 '(' 配平
        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    # 先补一个 ')' 让 need 变成偶数
                    res += 1
                    need -= 1
                need += 2  # 这个 '(' 需要两个 ')'
            else:  # ch == ')'
                need -= 1
                if need < 0:
                    # 右括号多了，补一个 '('
                    res += 1
                    # 当前这个 ')' 当作新 '(' 的第一个配对 ')'
                    need = 1  # 还需要一个 ')'

        return res + need
