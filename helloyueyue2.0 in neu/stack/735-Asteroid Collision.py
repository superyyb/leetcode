class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
         ->         <-
        5 10 8 1 2 -5 -1
        Stack
        for loop:
            Postive: add to the stack
            Negetive: while stack, compare with stack[-1]
                        1.stack[-1] + negetive == 0: pop
                        2.stack[-1] + negetive > 0: continue
                        3.stack[-1] + negetive < 0: pop then add
                     empty stack: add to the stack
        return stack
碰撞前提：只有 stack[-1] > 0（右行）且 asteroid < 0（左行）才会撞。
存活状态：用一个变量（如 alive）标记当前的负数行星是否还在。
同归于尽：如果相等，两边都消失，且 alive 变为 False。
        case: [-1,-1,-1]
        case: [2,-5]
        '''
        stack = []
        for ast in asteroids:
            alive = True  # 记录当前行星状态是否alive
            while alive and ast < 0 and stack and stack[-1] > 0:
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                alive = False
            if alive:
                stack.append(ast)
        return stack

