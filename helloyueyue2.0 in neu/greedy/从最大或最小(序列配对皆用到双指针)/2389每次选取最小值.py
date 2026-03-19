"""
greedy:
局部最优选择：
每次都优先选取当前数组中最小的元素
"""
#bruce force O(NLogN)+O(Q*N)
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            i = 0  # 这里的i起到计subsequence长度的作用，并且最大长度不超过len(nums)
            sub_sum = 0
            while i < len(nums):
                if sub_sum + nums[i] > q:
                    break
                sub_sum += nums[i]
                i += 1
            ans.append(i)
        return ans

#binary search O(NlogN) + O(Q*logN)
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        res = []
        for i in range(1, n):
            prefixSum[i] = nums[i] + prefixSum[i - 1]
        print(prefixSum)
        for query in queries:
            i, j = 0, n
            while i < j:
                mid = i + (j - i) // 2
                if prefixSum[mid] > query:
                    j = mid
                else:
                    i = mid + 1
            res.append(i)
        return res
