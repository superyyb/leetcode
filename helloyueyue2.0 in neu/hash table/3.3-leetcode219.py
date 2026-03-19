class Solution():
    def containsNearbyDuplicate(self,nums:list[int],k:[int])->bool:
        hash={}
        for i, num in enumerate(nums):
            if num in hash and i - hash[num]<=k:
                return True
            hash[num]=i
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))