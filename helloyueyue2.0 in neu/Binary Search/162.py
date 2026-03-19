class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return r
"""
用到mid+1 当最后一次循环时，l=r=mid,此时mid+1越界
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return r


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            # if nums[l] == nums[mid] and nums[r] == nums[mid]:
            #     l += 1
            #     r -= 1
            """
            [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
            [0,21] mid=10 nums[mid]=1
            [1,20] mid=10 nums[mid]=1
            [2,19] mid=10
            [3,18] 
            ...
            [11,10]
            """
            if nums[l] == nums[mid]:
                l += 1
            if nums[r] == nums[mid]:
                r -= 1

            while l < mid and nums[l] == nums[mid]:
                l += 1
                print(l)
            while r > mid and nums[r] == nums[mid]:
                r -= 1
                print(r)

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

