class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    #不同于lc26，最多出现两次，用hash记录出现次数，继续用双指针实现in-place移除
        '''
        Two-pointer
        1. One pointer traverses through the list
        2. Another pointer overwrites elements and stores the number of valid elements
        3. Use hashmap to store the freq of elements
        '''
        i, j = 0, 0
        hash={}
        while i < len(nums):
            if nums[i] not in hash:
                nums[j] = nums[i]
                j += 1
                hash[nums[i]] = 1
            elif hash[nums[i]] < 2:
                nums[j] = nums[i]
                j += 1
                hash[nums[i]] += 1
            i += 1
        return j