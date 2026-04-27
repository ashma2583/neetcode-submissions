class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n == '+':
                int1 = stack.pop()
                int2 = stack.pop()
                stack.append(int1 + int2)
            elif n == '-':
                int1 = stack.pop()
                int2 = stack.pop()
                stack.append(int2 - int1)
            elif n == '*':
                int1 = stack.pop()
                int2 = stack.pop()
                stack.append(int1 * int2)
            elif n == '/':
                int1 = (stack.pop())
                int2 = (stack.pop())
                stack.append(int(float(int2) / int1))
            else:
                stack.append(int(n))
            print(stack)
        
        return stack[0]
