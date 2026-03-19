class Solution:
    def removeDuplicates(self, strs: str) -> str:
        stack=[]
        for i in range(len(strs)):
            if stack and stack[-1]==strs[i]:
                stack.pop()
            else:
                stack.append(strs[i])
        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()
    s = "abbaca"
    result = sol.removeDuplicates(s)
    print(result)
