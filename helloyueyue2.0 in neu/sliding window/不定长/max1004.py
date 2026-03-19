class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        向右遍历时flip，如果flip次数用完，统计当前1的个数
        左边界收缩时，如果遇到被flip的元素，减去的同时还原其flip次数
        """
        left = 0
        max_ans = ans = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:  #扩
                k -= 1
            while k < 0 and left <= right: #不满足条件时缩左边界
                if nums[left] == 0:
                    k += 1
                left += 1
            ans = right - left + 1 #更新
            max_ans = max(max_ans, ans)
        return max_ans