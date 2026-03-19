class Solution:
    def evalRPN(self,tokens:list[str])->int:
        stack=[]
        """
            if token.isnumeric(): 不可以解决token是负数的情况，除非if token.lstrip("-").isnumeric():
                value=int(token)#str cannot be operated
                stack.append(value) 
        """
        for token in tokens:
            if token=="+":
                if len(stack) >= 2:
                    a=stack.pop()
                    b=stack.pop()
                    c=b+a
                    stack.append(c)
            elif token == "-":
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    c = b - a
                    stack.append(c)
            elif token == "*":
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    c = b * a
                    stack.append(c)
            elif token == "/":
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    c = int(b /a)
                    stack.append(c)
            else:
                stack.append(int(token))#简单明了 else囊括所有数字，包括负数，避开写isdigit()
        return stack.pop()#或者 stack[-1]

if __name__=="__main__":
    sol=Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(sol.evalRPN(tokens))
