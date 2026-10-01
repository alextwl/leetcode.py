'''
2026/10/01 daily challenge

stack + hash approach
'''


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


'''
stack + if-conditions only
'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            else:
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
        return not(stack)

