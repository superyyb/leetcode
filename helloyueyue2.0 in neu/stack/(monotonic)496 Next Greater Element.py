class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 一次性把 nums2 里所有元素 的next greater num都算出来，再按 nums1 去查。
        next_greater = {}
        res = [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                n = stack.pop()
                next_greater[n] = num
            stack.append(num)
        for i, num in enumerate(nums1):
            if num in next_greater:
                res[i] = next_greater[num]
        return res

    """
dict.get(key, default) 表示：
•	如果字典里存在 key → 返回对应的值。
•	如果字典里没有 key → 返回 default。

seen[num] = seen.get(num, 0) + 1
•	如果字典里已经有这个 num → 返回它当前的次数。
•	如果字典里还没有这个 num → 返回默认值 0。
•	再加 +1：把次数加一。
    """
