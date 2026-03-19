#yy思路：如果不存在两个A存在于字符串或不存在"LLL"在字符串，则返回true
from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        count=Counter(s)
        if "LLL" in s or count["A"]>=2:
            return False
        else:
            return True

#q其实不用专门赋值出一个字典,直接使用s.count()的返回值就可以
'''
解法二：one-line solution
return s.count("A")<2 and "LLL" not in s
'''