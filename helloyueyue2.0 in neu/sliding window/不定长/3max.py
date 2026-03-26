#Mar 19复盘
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Sliding window with hashmap
        1.Maintain a valid window [left, right]
        2.Expand right pointer to include new characters
        3.If a duplicate is found (freq > 1), shrink the window by moving left pointer until the window becomes valid again
        4.Track the maximum window size
        '''
        freq = {}
        left = 0
        n = len(s)
        max_len = 0
        for right in range(n):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = count = 0
        n = len(s)
        seen = set()
        left = 0
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            count = right - left + 1
            max_count = max(max_count, count)
        return max_count
    """
    1.for循环：右指针 right 向右扩张窗口，加入新字符 s[right]。
    2.如果该字符已在窗口中（即在 seen 集合里），就不断让左指针left右移，
      并同时从 seen 中移除 s[left]，直到窗口内不再有重复。
    """

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
    当我们遇到一个新字符 char = s[right] 时：
	•如果它没出现过，窗口可以扩展；
	•如果它出现过，把左边界移动到上一个重复字符的右边，从而“跳过”旧的那个重复。
        """
        max_count = 0
        seen = {}#seen的value始终记录这个字符最近一次出现的index
        left = 0
        n = len(s)
        for right, char in enumerate(s):#right bound->scan
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            max_count = max(max_count, right - left + 1)
        return max_count