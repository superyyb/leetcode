class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        ans = -1
        while l <= r:
            count = 0
            mid = l + (r - l) // 2
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans
    """
    [1,1,4,2,3]
    l=1,r=4 1,2,3,4 mid = 2 count的有3个，所以重复值一定在[1...2]中
    """

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        while l < r:
            count = 0
            mid = l + (r - l) // 2
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                r = mid
            else:
                l = mid + 1
        return l