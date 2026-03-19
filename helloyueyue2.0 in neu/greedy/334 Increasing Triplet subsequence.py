#❌解，题目要求可以不连续
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #Find one increasing triplet -> return True else False
        # #mono stack
        # stack = []
        # for num in nums:
        #     while stack and num < stack[-1]:
        #         stack.pop()
        #     stack.append(num)
        #     if len(stack) == 3:
        #         return True
        # return False
        smallest = nums[0]
        length = 1
        max_length = 0
        for num in nums:
            if num > smallest:
                length += 1
                max_length = max(max_length, length)
                if max_length >= 3:
                    return True
            else:
                length = 1
                smallest = num
        return False

#DP解法 O(n2)会超时
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        1.dp[i]: The length of longest subsequences which ends by nums[i]
        2.Formula(How to reach dp[i]):
        If there exists any dp[j] before dp[i] that nums[j] < nums[i], dp[i] + 1
        3.Intialize dp[0] = 1
        4.Travseral order:From start to end
        '''
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] >= 3:
                    return True
        return False

