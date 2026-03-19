#Feb23复盘
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Sliding window with a fixed length
        1.Use a hashmap to store the freq of s1
        2.Use another hashmap to store the window
        3.Traverse through s2, check if they match, return True
        '''
        target = Counter(s1)
        window = Counter()
        left = 0
        for right, char in enumerate(s2):
            window[char] += 1
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                left += 1
            # Counter 在做 == 比较时，会忽略 value 为 0 的键。所以没有 del 也能 AC
            # 但是坚持写del 代码更干净 不会出现{ 'b':0, 'c':0, 'd':0, 'e':0, ...}
            if target == window:
                return True
        return False


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #sliding window of fixed length
        n = len(s1)
        target = Counter(s1)
        window = Counter()
        left = 0
        for right, char in enumerate(s2):
            window[char] += 1
            if right - left + 1 > n:
                window[s2[left]] -= 1#we don't need to del if window[s2[left]] == 0
                #because it is Counter()
                left += 1
            if target == window:
                return True
        return False