class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:#num is the start
                length = 1#reset the length
                while num + 1 in num_set:#continue the sequence
                    num += 1
                    length += 1
                max_length = max(max_length, length)
        return max_length
    '''
    if:是起点么
    while:还能继续么
    '''
