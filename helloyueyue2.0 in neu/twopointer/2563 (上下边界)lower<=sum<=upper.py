class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def lower_than(n:int, bound:int):
            count = 0
            i, j = 0, n - 1
            while i < j:
                if nums[i] + nums[j] <= bound:
                    count += j-i
                    i += 1
                else:
                    j -= 1
            return count
        return lower_than(len(nums),upper) - lower_than(len(nums),lower-1)
        #注意要减去所有<lower的数，因此bound要变成lower-1

