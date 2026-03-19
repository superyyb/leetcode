class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        #要找到in_deg为0的点
        res = []
        in_deg = [0] * n
        for u, v in edges:
            in_deg[v] += 1
        for i, d in enumerate(in_deg):
            if d == 0:
                res.append(i)
        return res