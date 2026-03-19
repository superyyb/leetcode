class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            stack = []
            for char in string:
                if stack and char == '#':
                    stack.pop()
                else:
                    stack.append(char)
            return stack
        return helper(s) == helper(t)

#twopointer O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #time O(n+m) space O(1)
        i, j = len(s) - 1, len(t) - 1
        skip_s = skip_t = 0
        while i >= 0 or j >= 0:#为什么不是and s = "a#"  t = ""
            # 处理 s 的下一个有效字符
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break  # s[i] 现在是一个有效字符

            # 处理 t 的下一个有效字符
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break  # t[j] 现在是一个有效字符

            # 比较当前有效字符
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            else:
                # 有一个已经没字符了，另外一个还有有效字符
                if i >= 0 or j >= 0:
                    return False

            i -= 1
            j -= 1

        return True
