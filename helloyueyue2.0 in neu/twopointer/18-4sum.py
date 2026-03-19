class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #for loop + two-pointer
        nums.sort()#[-2, -1, 0, 0, 1, 2]
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):#❌写成range(n - 2)
                if j > i + 1 and nums[j] == nums[j - 1]:#❌写成j > 0
                    continue
                k, p = j + 1, n - 1
                while k < p:
                    curr_sum = nums[i] + nums[j] + nums[k] + nums[p]
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[k], nums[p]])
                        k += 1
                        p -= 1
                        while k < p and nums[k] == nums[k - 1]:
                            k += 1
                        while k < p and nums[p] == nums[p + 1]:
                            p -= 1
                    elif curr_sum > target:
                        p -= 1
                    else:
                        k += 1
        return res