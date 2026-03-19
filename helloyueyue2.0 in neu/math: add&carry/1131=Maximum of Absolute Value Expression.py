class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        ∣a∣+∣b∣+∣c∣ = max(±a±b±c)

        |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
        = max(±(arr1[i]−arr1[j])±(arr2[i]−arr2[j])±(i−j))
        =max((±arr1[i]±arr2[i]±i)−(±arr1[j]±arr2[j]±j))

        '''
        ans = 0
        # 4 sign choices for arr1 and arr2
        for s1, s2 in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            # expression: s1*arr1[i] + s2*arr2[i] + i
            mx = float("-inf")
            mn = float("inf")
            for i in range(len(arr1)):
                v = s1 * arr1[i] + s2 * arr2[i] + i
                mx = max(mx, v)
                mn = min(mn, v)
            ans = max(ans, mx - mn)

            # expression: s1*arr1[i] + s2*arr2[i] - i
            mx = float("-inf")
            mn = float("inf")
            for i in range(len(arr1)):
                v = s1 * arr1[i] + s2 * arr2[i] - i
                mx = max(mx, v)
                mn = min(mn, v)
            ans = max(ans, mx - mn)

        return ans