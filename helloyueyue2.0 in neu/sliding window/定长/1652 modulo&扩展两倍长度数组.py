class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        codes = code + code # 构造 长度 2n 的数组
        res = [0] * n #注意这么写更简洁 后面直接res[i] = total，相较于res=[],res.append(code[i])
        if k == 0:
            return res
        if k > 0:
            for i in range(n):
                total = 0
                for j in range(i + 1, i + k + 1):
                    total += codes[j]
                res[i] = total
        if k < 0:
            for i in range(n):
                total = 0
                for j in range(i + n + k, i + n):
                    total += codes[j]
                res[i] = total
        return res

#用modulo: index//k
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        if k > 0:
            for i in range(n):
                total = 0
                for j in range(1, k + 1):
                    idx = (i + j) % n
                    total += code[idx]
                ans[i] = total
        else:
            m = -k
            for i in range(n):
                total = 0
                for j in range(1, m + 1):
                    idx = (i - j) % n  # Python 里负数 % n 会自动加上 n
                    total += code[idx]
                ans[i] = total
        return ans