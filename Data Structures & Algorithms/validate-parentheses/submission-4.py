class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'}':'{', ')': '(', ']': '['}

        for p in s:
            if p in valid:
                if stack and stack[-1] == valid[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return True if not stack else False