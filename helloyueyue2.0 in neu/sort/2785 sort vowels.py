#time: O(n+k(log(k))) space: O(n)
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        list_s = list(s)
        for char in s:
            if char in "AEIOUaeiou":
                vowels.append(char)
        vowels.sort()#可以sort by ASCII code
        if vowels == []:
            return s
        j = 0
        for i in range(len(list_s)):
            if s[i] in "AEIOUaeiou":
                list_s[i] = vowels[j]
                j += 1
        return "".join(list_s)