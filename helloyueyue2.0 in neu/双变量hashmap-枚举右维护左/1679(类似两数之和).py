class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        count = 0
        for num in nums:
            if k - num in seen:
                count += 1
                seen[k - num] -= 1
                if seen[k - num] == 0:
                    del seen[k - num]
            else:#配对成功时，不要把这个 num 再放进 seen，它已经和 k-num 一起“被用掉”了。
                seen[num] = seen.get(num, 0) + 1
        return count