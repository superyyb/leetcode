class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        count = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
            else:
                if not stack:
                    if i != len(s) - 1 and s[i + 1] == ')':
                        count += 1
                        i += 1  # Skip next ')'
                    else:
                        count += 2
                else:
                    if i != len(s) - 1 and s[i + 1] == ')':
                        stack.pop()
                        i += 1
                    else:
                        count += 1
                        stack.pop()
            i += 1
        return count + len(stack) * 2  # Each unmatched '(' needs two ')'

class Solution:
    def minInsertions(self, s):
        res = right = 0
        for c in s:
            if c == '(':
                if right % 2:#right为奇数
                    right -= 1
                    res += 1
                right += 2#每出现(，需要配两个)
            if c == ')':
                right -= 1
                if right < 0:
                    right += 2
                    res += 1
        return right + res
    '''
    res = 我们中途插入的括号数
    right = 到最后还欠的右括号数（需要补的 ')'）
    '''