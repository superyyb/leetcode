class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #从小到大排序，每次反转最小的数
        nums = sorted(nums)# [-4,-3,-1,2,5] k = 2
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = - nums[i]
                k -= 1
        nums = sorted(nums)
        if k > 0 and k % 2 != 0:
            nums[0] = -nums[0]
        return sum(nums)

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #设立min_heap 每次取出最小值取反
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        while k > 0:
            minimum = heapq.heappop(heap)
            heapq.heappush(heap, -minimum)
            k -= 1
        return sum(heap)