class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        固定长度窗口：每right进来一个，就必定left推出一个
        output: max number of vowels
        """
        n = len(s)
        vowels = set("aeiou") #检查是否在集合中
        #先统计第一个长度为k的窗口
        curr = 0
        for i in range(min(k, n)): #考虑k比n大的情况
            if s[i] in vowels:
                curr += 1
        max_v = curr
        #从right = k开始，每次右移一位
        for right in range(k, n):
            if s[right] in vowels:
                curr += 1
            if s[right - k] in vowels:
                curr -= 1
            max_v = max(max_v, curr)
        return max_v

#类似双指针left-right
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = set("aeiou")
        left = 0
        curr = 0
        for right in range(min(n,k)):
            if s[right] in vowels:
                curr += 1
        max_v = curr
        for right in range(k,n):
            if s[right] in vowels:
                curr += 1
            if s[left] in vowels:
                curr -= 1
            left += 1
            max_v = max(max_v, curr)
        return max_v

#right 从0一路跑到尾，扩窗、缩窗、更新答案都在同一个 for loop里完成
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = set("aeiou") #检查是否在集合中
        left = 0
        curr = 0
        max_v = 0
        for right in range(n): #不断向右扩窗
            if s[right] in vowels:
                curr += 1
            if right - left + 1 > k: #长度大于k：缩窗
                if s[left] in vowels:
                    curr -= 1
                left += 1
            if right - left + 1 == k: #长度等于k：更新max_v
                max_v = max(max_v, curr)
        return max_v

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = set("aeiou")
        max_count = count = 0
        if k == 0:
            return 0
        else:
            for i in range(n):
                if s[i] in vowels:
                    count += 1
                if i < k - 1:
                    continue
                max_count = max(max_count, count)
                if s[i - k + 1] in vowels:
                    count -= 1
        return max_count