class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two-pointer
        #i traverses through the list, j rewrites the list
        i, j = 0, 0
        visited = set()
        while i < len(nums):
            if nums[i] not in visited:
                nums[j] = nums[i]
                j += 1
                visited.add(nums[i])
            i += 1
        return j