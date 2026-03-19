#解法1：直接用find()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
           :type haystack: str
           :type needle: str
           :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
sol=Solution()
haystack1="i love you baby"
needle1="you"
haystack2="i love you baby"
needle2="him"
print(sol.strStr(haystack1,needle1))
print(sol.strStr(haystack2,needle2))

#解法2：花式切片（简便）
def strStr(haystack, needle):
    needle_len = len(needle)
    haystack_len = len(haystack)
    if needle_len == 0:
        return 0
    for i in range(haystack_len - needle_len + 1):
        # haystack="sadbutsad", needle="sad" 需要比较6次（8-3+1）
        if haystack[i:i + needle_len] == needle:#切片比较 用i来轮换比较的位置
            return i
    return -1 #当for循环中的所有迭代都完成没有找到匹配条件时，直接执行return -1
# 测试示例
print(strStr("sadbutsad", "sad"))  # 输出: 0
print(strStr("leetcode", "leeto"))  # 输出: -1