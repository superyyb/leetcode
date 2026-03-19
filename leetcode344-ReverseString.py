#如何不占用额外空间实现序列的元素反转
#双指针法
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,j=0,len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i += 1
            j -= 1
sol=Solution()
s1=["h","e","l","l","o"]
sol.reverseString(s1)
print(s1)

        #我的错误解法：
        # for i,j in len(s):
        #     s[i]=s[j]
        #     i+=1
        #     j+=1
        # return s
