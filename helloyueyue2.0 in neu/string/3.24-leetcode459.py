#two pointers
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i=0
        for j in range(len(list(s))):
            if list(s)[j]==list(s)[i]:

