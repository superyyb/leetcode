class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":#keep adding until a "]"
                stack.append(char)
            else:
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str#⚠️不能写成curr_str += stack.pop()
                stack.pop()#pop "["
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num#⚠️不能写成curr_num += stack.pop()
                curr_str *= int(curr_num)
                stack.append(curr_str)
        return "".join(stack)