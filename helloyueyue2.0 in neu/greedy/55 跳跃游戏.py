#Jan6复盘
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Greedy algo
        1.Check whether can get to position i
        2.Calculate the farthest distance every position can get
        3.If farthest distance >= len(nums) - 1, return True. Otherwise False
        '''
        n = len(nums)
        farthest = 0
        for i in range(n):
            if farthest < i:#⚠️必须放在 更新 farthest 之前
                return False
            farthest = max(farthest, nums[i] + i)#更新farthest的前提是i <= farthest
            if farthest >= n - 1:
                return True

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i, j = 0, 0 #双指针i表示目前用的position的fuel，j表示可以到达的position
        while nums[i] > 0:
            nums[i] -= 1
            j += 1
            if nums[j] > nums[i]:
                nums[i] = nums[j]
            if j >= len(nums) - 1:
                return True
        return False
"""
刚看到本题一开始可能想：当前位置元素如果是 3，我究竟是跳一步呢，还是两步呢，还是三步呢，究竟跳几步才是最优呢？
其实跳几步无所谓，关键在于可跳的覆盖范围！
每次移动取最大跳跃步数（得到最大的覆盖范围），每移动一个单位，就更新最大覆盖范围。

"""

#或者可以先计算最大步数，再判断，但是要注意len(nums) == 1的base case
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Calculate the max distance u can reach in every position
        farthest = 0 #the max distance can reach in every position
        if len(nums) == 1:
            return True
        for i, step in enumerate(nums):
            farthest = max(farthest, i + step)
            if i >= farthest:
                return False
            if farthest >= len(nums) - 1:
                return True

#DP 会超时 因为最坏O(n2) 最优解还是贪心
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):  # 遍历所有的i直到最后一位
            for j in range(i):  # 遍历所有j < i 看是否有j可以到达i
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]

    """
一旦找到一个可行的 j，我们就能确定 dp[i] = True。
•	我们已经知道 “可以到达 i”；
•	继续循环后面的 j 没意义；
•	所以直接 break 跳出内层循环
    """