class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # pointers time and space:O(n)
        n = len(nums)
        res = []
        i = 0
        while i < n:
            if nums[i] < pivot:
                res.append(nums[i])
            i += 1
        for num in nums:
            if num == pivot:
                res.append(num)
        i = 0
        while i < n:
            if nums[i] > pivot:
                res.append(nums[i])
            i += 1
        return res