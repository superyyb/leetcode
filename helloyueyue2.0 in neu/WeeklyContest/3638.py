class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        max_val = 0
        count = 0
        for i in range(len(weight)):
            if weight[i] >= max_val:
                max_val = weight[i]
            else:
                count += 1
                max_val = 0
        return count