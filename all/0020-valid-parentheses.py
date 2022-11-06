class Solution:
    def isValid(self, s: str) -> bool:
        openbrackets = '([{'
        close2open = {')': '(',
                      ']': '[',
                      '}': '{'}
        stack = []
        for c in s:
            if c in openbrackets:
                stack.append(c)
            elif c in close2open:
                if not stack:
                    return False
                opener = stack.pop()
                if opener != close2open[c]:
                    return False
        
        if stack:
            # stack is not empty. opened bracket exists.
            return False
        # all brackets are closed.
        return True
