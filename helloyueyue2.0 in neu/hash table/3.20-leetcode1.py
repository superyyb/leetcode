class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash={}
        for i in range(len(nums)):
            if target-nums[i] in hash:
                return [i,hash[target-nums[i]]]
            hash[nums[i]]=i
        return []

if __name__=="__main__":
    sol=Solution()
    nums=[2,7,11,15]
    print(sol.twoSum(nums,target=9))