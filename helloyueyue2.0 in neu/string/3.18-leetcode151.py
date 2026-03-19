"""
class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        lst.reverse()
        print(lst)
        t=" ".join(lst)
        return t
"""
#双指针
class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        i,j=0,len(lst)-1
        while i<j:
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
            j-=1
        return " ".join(lst)


if __name__=="__main__":
    s = "a good   example"
    sol=Solution()
    print(sol.reverseWords(s))

