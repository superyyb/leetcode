class Solution: #bruce force time: O(n2)
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + arr[i]
        total = 0
        for length in range(1, n + 1, 2):#枚举所有奇数长度子数组
            for start in range(0, n - length + 1):
                end = start + length
                total += prefixSum[end] - prefixSum[start]
        return total

class Solution:#用到了sum() time: O(n3)
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        for start in range(n):
            for end in range(start, n):
                sub = arr[start: end + 1]
                if len(sub) % 2 != 0:
                    total += sum(sub)
        return total