class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort() #sorted:[-1,1,1,2,3]
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] >= target:
                j -= 1
            else:
                count += j-i
                i += 1
        return count

    """
    为什么要加i += 1
    所有的 j’ ∈ [i+1, j] 都是合法的，所以此时我们能统计的对数是：(j - i) 个。
    然后我们必须移动 i 指针，否则下一轮你会重复使用这个 i 值 ，会导致无限循环，或者重复计数。
    """