class Solution:
#遇到递增/递减斜坡怎么办，遇到平地怎么办
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        count = 1#默认第一个元素计入count
        curr_diff = 0
        pre_diff = 0
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i - 1]
            if curr_diff * pre_diff <= 0 and curr_diff != 0:
                count += 1
                pre_diff = curr_diff#必须在if里面
        return count

"""
为什么每次更新pre_diff必须是确实出现波动之后：
反例：1-1-2-2-3-3 遇到递增中夹着平地，最多只能取长度 2（比如 [1,3]）。但代码会数成3，因为每次遇到 == 都把 pre_diff 清零，后面的上坡又被当成新的“拐”。
"""