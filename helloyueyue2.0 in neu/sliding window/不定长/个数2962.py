class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        向右扩展：找最大元素，记录每个元素的出现次数，>=k则加入ans
        缩左边界：通过max()直接找到nums的最大值
        [1,3,2,3,3] 比如找到了[3,3]，那么left往左一直到0，都是可行的subarray
        """
        left = 0
        ans = 0
        count = 0
        n = len(nums)
        max_val = max(nums)
        for right, x in enumerate(nums):
            if x == max_val:
                count += 1
            while count == k:
                if nums[left] == max_val:
                    count -= 1
                left += 1 #每次都是这里缩进错误，left += 1是每次while循环都要做的操作，因为这个while是非法区间
            ans += left
        return ans