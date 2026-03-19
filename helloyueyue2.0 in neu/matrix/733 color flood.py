#time space: O(m*n)
'''
        if image[i][j] == color:
            return
等价于   visited数组
等价于
        if original == color:
            return image

'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        visit = [[False] * n for _ in range(m)]
        original_color = image[sr][sc]
        def dfs(r, c):
            image[r][c] = color#操作
            visit[r][c] = True#已访问
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visit[nr][nc] and image[nr][nc] == original_color:
                    dfs(nr, nc)
        dfs(sr, sc)
        return image

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return []
        m = len(image)
        n = len(image[0])
        standard = image[sr][sc]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != standard or image[i][j] == color:
                return #要么加上visited数组，要么加上if image[i][j] == color: return 判断
            image[i][j] = color
            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                dfs(nr, nc)

        dfs(sr, sc)
        return image

#精简
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        m, n = len(image), len(image[0])
        def dfs(r, c):
            # base case
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != original:
                return
            image[r][c] = color
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                dfs(r + dr, c + dc)
        dfs(sr, sc)
        return image
    #⚠️visit 数组其实没必要，每次都会把访问过的像素改成 color，自然就避免了重复访问。
