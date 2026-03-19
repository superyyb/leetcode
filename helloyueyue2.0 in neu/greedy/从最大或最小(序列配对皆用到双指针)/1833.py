class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        print(costs)
        count = 0
        for i, cost in enumerate(costs):
            if coins - cost >= 0:
                coins -= cost
                count += 1
        return count

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        print(costs)
        count = 0
        for i, cost in enumerate(costs):
            if coins < cost:
                break
            coins -= cost
            count += 1
        return count