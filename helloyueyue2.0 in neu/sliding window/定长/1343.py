class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = sum = 0
        n = len(arr)
        for i, x in enumerate(arr):
            sum += x
            if i < k - 1: #扩
                continue
            if sum >= k*threshold: #判断更新
                count += 1
            sum -= arr[i - k + 1] #缩
        return count