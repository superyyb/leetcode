#如何实现 移除所有非字母数字字符并将大写字母转换为小写字母
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #大写字母转换为小写字母
        s = re.sub(r'[^a-z0-9]', '', s) #移除所有非字母数字字符
        return s==s[::-1] #检查是否为回文
sol=Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
print(sol.isPalindrome(" "))

#解法2：双指针，只用遍历一次
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1 #i 和 j 是两个指针，分别初始化为字符串 s 的开头和结尾。
        while i < j: #循环持续进行直到 i 和 j 相遇。
         #以下这两个while循环用来跳过非字母数字的字符
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
        """
        !!!abcba!!! while i < j and not s[i].isalnum():就能连续跳过左边3个！
        """
        #以下这个if条件用来比较字母是否相同
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum()
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue  # 立即跳过剩下的步骤，重新进入循环
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


