class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip() #去掉末尾空格
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break
            count += 1
        return count

#指针从后往前跳过空格
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":#Skip the spaces
            i -= 1
        count = 0
        while i >= 0 and s[i] != " ":#Count the answer
            count += 1
            i -= 1
        return count