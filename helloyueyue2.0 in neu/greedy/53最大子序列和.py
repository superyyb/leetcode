class Solution:
    #当subSum为负数时立刻放弃 重新计算
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf") #初始化结果
        subSum = 0
        for i in range(len(nums)):
            subSum += nums[i]
            if subSum >= res:# 取区间累计的最大值（相当于不断确定最大子序终止位置）
                res = subSum
            if subSum <= 0:# 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
                subSum = 0
        return res

"""
这两个if顺序不能换，参考[-1]作为例子，调换if会输出null
可以再思考一下如果是全负数组[-2,-3,-4,-5]会怎么运行
"""

#9.8复盘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float("-inf")
        curr_sum = 0
        for num in nums:
            curr_sum += num
            largest_sum = max(largest_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0 #舍弃前面为负数的sum，重新累加
        return largest_sum

#Jan 6 复盘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Greedy algo
        1.Calculate the curr_sum. If curr_sum < 0, reset it to 0.
        2.Store and update the largest_sum
        '''
        #❌解
        largest_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum < 0:
                curr_sum = 0
            largest_sum = max(largest_sum, curr_sum)#⚠️必须放在reset之前
        return largest_sum

#Feb 2复盘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Greedy
        1.Store largest_sum, curr_sum
        2.If cur_sum < 0: reset it to 0
        '''
        largest_sum, curr_sum = float('-inf'), 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            largest_sum = max(largest_sum, curr_sum)
        return largest_sum