#logic:if curr char is smaller than char in stack,
# and the appearance of char in stack > 0, remove the char in stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        freq = {}
        seen = set()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        for char in s:
            freq[char] -= 1 #⚠️删除freq一定要在continue之前！！！
            if char in seen: #⚠️很容易漏这句（对于每个char都要检查是否已经出现）
                continue
            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(char)
            seen.add(char)
        return ''.join(stack)

