class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 1
            i += 1


class Solution:  # 先数有几个zero，在队列末尾留出几个空位
    def duplicateZeros(self, arr: List[int]) -> None:
        zero = 0
        for a in arr:
            if a == 0:
                zero += 1
        i, j = len(arr) - 1, zero + len(arr) - 1
        while i < j:
            if j < len(arr):
                arr[j] = arr[i]  # 写入第一个0
            if arr[i] == 0:
                j -= 1
                if j < len(arr):
                    arr[j] = 0  # 写入第二个0
            i -= 1
            j -= 1
