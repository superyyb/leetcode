"""
这道题不可以用hash记录数量，因为题目不仅要求括号数量匹配，还要保证匹配的顺序
用stack顺序严格受控，像 "([)]" 就会返回 False。
"""
class Solution:
    def isValid(self, s: str) -> bool:
        """
        用dict建立括号之间匹配关系
        key: 所有右括号
        value：所有左括号
        """
        stack = []
        mapping = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in mapping: #遇到右括号
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:#遇到左括号
                stack.append(ch)
        return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(":")", "[":"]", "{":"}"}
        for bracket in s:
            if bracket in mapping.keys():
                stack.append(bracket)
            else:
                if not stack or mapping[stack[-1]] != bracket:
                    return False
                stack.pop()#⚠️先“检查是否匹配”，匹配才pop
        return not stack
