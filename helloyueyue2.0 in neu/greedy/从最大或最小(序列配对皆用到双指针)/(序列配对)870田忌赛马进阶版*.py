class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #田忌赛马；永远拿最大的和另一个序列最大的比，比不过就拿最小的补上去
        nums1.sort()
        n = len(nums1)
        res = [0] * n
        sort_nums2 = sorted(((val, idx) for idx, val in enumerate(nums2)), reverse = True) #[(32,2),(25,1),(13,0),(11,3)]
        i, j = 0, n - 1
        for val, idx in sort_nums2:
            if nums1[j] > val:
                res[idx] = nums1[j]
                j -= 1
            else:
                res[idx] = nums1[i]
                i += 1
        return res