class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        add = 0
        for char in s:
            if char == ")":
                if not stack or stack.pop() != "(":
                    add += 1
            else:
                stack.append(char)
        return add + len(stack)
    """
    ⚠️
    1.)多了：用add计算
    2.(多了：用len(stack)计算
    """