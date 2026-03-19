class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        转为前缀和数值问题 如符合为0，不符为1
        索引 0 没有前驱元素可比，约定 bad[0] = 0
        bad[i] 标记的是 “位置 i 和 i−1 这对相邻元素是否同奇偶”
        [4,2,3,5] -> bad[0, 1, 0, 1] -> P[0, 1, 1, 2]
        这里的前缀和其实是区间 [l..r] 里的坏点数 = P[r] - P[l]
        [0, 2]: P[2] - P[0] = 1 “坏点数 > 0”-> False
        [2, 3]: P[3] - P[2] = 1 “坏点数 > 0”-> False
        “坏点数 = 0”才为True
        """
        bad = [0] * len(nums)
        res = []
        for i in range(1, len(nums)):
            bad[i] = bad[i - 1]  # bad[i]=1 表示 nums[i] 和 nums[i-1] 同奇偶，否则 0
            bad[i] = 1 if (nums[i] - nums[i - 1]) % 2 == 0 else 0

        Prefix = [0] * len(nums)
        Prefix[0] = bad[0]
        for i in range(1, len(nums)):
            Prefix[i] = Prefix[i - 1] + bad[i]
        for l, r in queries:  # 序列解包
            res.append((Prefix[r] - Prefix[l]) == 0)
        return res
    """
      •什么时候用 P 长度 n+1？
    当 P[i] 定义为「原数组前 i 个元素之和」时，P[0] = 0，
    P[1]=nums[0]，…，下标自然跑到 n。
    此时「区间和 = P[r+1] − P[l]」
      •什么时候用 P 长度 n？
    当你先映射出一个与原数组等长的辅助数组 A （比如每个位置的比较结果），
    并想直接对这个 A 做前缀和时，P 就跟 A 等长；
    此时「区间和 = P[r] − P[l]」

    序列解包：
    for x, y in some_list: 要求 some_list 的每个元素本身也是一个可迭代的、
    且长度和你要解包的变量数相同的序列（比如列表或元组）。
    """