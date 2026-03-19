#binary search
class Solution: #O(nlogn)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)): #[2,7,11,15]
            val = target - numbers[i]
            l, r = i+1, len(numbers) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if val == numbers[mid]:
                    return [i+1,mid+1] #index starts from 1
                elif val > numbers[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

#hashmap
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            if target - num in seen:
                return [seen[target - num] + 1, i + 1]
            seen[num] = seen.get(num, 0) + i
