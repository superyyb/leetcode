class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    # prefixSum[i] = nums[0] + ... + nums[i]
    # prefixSum[0] = 1 prefixSum[1] = 2 prefixSum[2] = 3
        curr_Sum = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1
        for num in nums:#[1, -1, 0]
            curr_Sum += num
            need = curr_Sum - k
            if need in freq:
                count += freq[need]
            freq[curr_Sum] += 1
            print(count,freq)
        return count