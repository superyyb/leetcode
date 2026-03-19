class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        res = [False] * n
        max_candy = max(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= max_candy:
                res[i] = True
        return res

#optimized
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''
       candies = [2,3,5,1,3], extraCandies = 3, max(candies) = 5
       1.Use a for loop to let the max number minus every other number
       2.Get a diff array  diff = [3,2,0,4,2]
       3.For loop: Compare diff to extraCandies, diff > extra:True  else:False
        '''
        max_candy = max(candies)
        for i, candy in enumerate(candies):
            if max_candy - candy <= extraCandies:
                candies[i] = True
            else:
                candies[i] = False
        return candies
