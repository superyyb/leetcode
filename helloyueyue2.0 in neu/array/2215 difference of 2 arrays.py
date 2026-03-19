class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Output:[[num not in nums2], [num not in nums1]]
        # 将列表转为集合（去重且提高查找速度）
        # Initialize an empty list
        answer = [[], []]
        nums1 = set(nums1)
        nums2 = set(nums2)
        for num in nums1:
            if num not in nums2:
                answer[0].append(num)
        for num in nums2:
            if num not in nums1:
                answer[1].append(num)
        return answer

#Easy method
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        # 使用差集运算符：
        return [list(s1 - s2), list(s2 - s1)]