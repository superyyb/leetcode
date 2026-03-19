class Solution:#hashtable
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        res = []
        for num in nums1:
            if num not in hash:
                hash[num] = 1 #{1:2,2:2}
            else:
                hash[num] += 1
        for num in nums2:
            if num in hash:
                res.append(num)
                if hash[num] > 1:
                    hash[num] -= 1
                elif hash[num] == 1:
                    del hash[num]
        return res

#双指针法：比较指针 i 和指针 j 的值大小，若两个值不等，则数字小的指针，往右移一位。
# 若指针 i 和指针 j 的值相等，则将值放入res。
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res
