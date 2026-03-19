#Feb23复盘 不要用curr_len, 用right - left + 1
from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        '''
        longest subarray: sliding window with a unfixed length
        1.Set a hashmap to store the frequency of each number
        2.Compare with k, if > k, shrink the window starting from left
        3.Update the max length
        '''
        left = 0
        freq = Counter()
        max_len, curr_len = 0, 0
        for right, num in enumerate(nums):
            freq[num] += 1
            curr_len += 1
            while freq[num] > k:
                freq[nums[left]] -= 1
                curr_len -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            max_len = max(max_len, curr_len)
        return max_len

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        检查每个字符在哈希表中出现频率
        """
        n = len(nums)
        seen = {}
        left = 0
        max_ans = ans = 0
        for right, x in enumerate(nums):
            if x not in seen:
                seen[x] = 1
            else:
                seen[x] += 1
            while seen[x] > k: #while内是不满足条件的
                seen[nums[left]] -= 1
                left += 1
            ans = right - left + 1
            max_ans = max(max_ans, ans)#结束while后即重新满足条件后再更新max_ans
        return max_ans