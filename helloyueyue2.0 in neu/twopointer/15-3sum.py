class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #三变量 先用for循环固定一个数，再用对撞指针确定另外两个数
        #用不同的方式跳过重复的数：
        # 1.for loop + continue
        # 2.while loop + 指针前进或后退
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue #跳过重复的数
            target = - nums[i]
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 #跳过重复的数
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1 #跳过重复的数
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return res
"""
j/k 的去重要在“移动指针之后、下一轮比较之前”做
"""