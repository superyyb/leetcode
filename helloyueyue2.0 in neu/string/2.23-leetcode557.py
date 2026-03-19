"""
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        for idx in range(len(s_list)):
            word= list(s_list[idx])
            print(word)
            i = 0
            j = len(word) - 1
            while i<j:
                word[i],word[j]=word[j],word[i]
                i+=1
                j-=1
            s_list[idx]="".join(word)
        return " ".join(s_list)

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.split()
        for idx in range(len(s_list)):
            word=s_list[idx]
            reversed_word=word[::-1]
            s_list[idx]="".join(reversed_word)
        return " ".join(s_list)
sol=Solution()
s="Let's take LeetCode contest"
result=sol.reverseWords(s)
print(result)