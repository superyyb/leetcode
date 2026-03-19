class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        if len(str1) == len(str2):#After the recursion
            return str1
        if len(str1) > len(str2):#str1:'ABABABABABAB'. str2:'ABAB'
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return self.gcdOfStrings(str1, str2[len(str1):])
    '''
    Keep recursing until meet the condition:
    if len(str1) == len(str2):
        return str1
    '''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Try every possible length of divisor
        min_len = min(len(str1), len(str2))
        for length in range(min_len, 0, -1):
            if len(str1) % length == 0 and len(str2) % length == 0:
                pattern = str1[:length]
                if pattern * (len(str1) // length) == str1 and pattern * (len(str2) // length) == str2:
                    return pattern

        return ""

