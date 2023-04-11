'''
2023/04/11 daily challenge

stack approach
'''

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)

