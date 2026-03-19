class Solution:#不好用双指针，无法同时到达平衡点
    def pivotIndex(self, nums: list[int]) -> int:
        i=0
        total_sum = sum(nums)
        left_sum=0
        while i<len(nums):
            right_sum = total_sum - left_sum - nums[i]
            if right_sum==left_sum:
                return i
            left_sum+=nums[i]
            i+=1
        return -1
if __name__=="__main__":
    nums = [2,1,-1]
    sol=Solution()
    print(sol.pivotIndex(nums))


