class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')' : '(', '}': '{', ']' : '['}

        for i in s: 
            if i in match: 
                if not stack or stack[-1] != match[i]: 
                    return False
                else: 
                    stack.pop()
            else: 
                stack.append(i)
        
        return not stack