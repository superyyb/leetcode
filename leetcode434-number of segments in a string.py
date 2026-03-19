#yy思路：
#int()=n,即str中有n-1个空格，用counter()把str创建为字典，输出" "对应的value，即几个空格
from collections import Counter
class Solution:
    def countSegments(self, s: str) -> int:
        s_count=Counter(s)
        # if s == "":
        #     return 0#
        # for char in s_count:
        #     if char==" ":
        #         return s_count[char]+1
        # n=int(s_count[char])
        # return n
        if s=="":
            return 0
        if ' ' in s_count:
            return s_count[' ']+1  # 返回空格 ' ' 在字符串 s 中出现的次数
        else:
            return 1  # 如果字符串中没有空格，则返回 0
sol=Solution()
print(sol.countSegments("Hello, my name is John"))
print(sol.countSegments("Hello"))