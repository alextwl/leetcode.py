'''
2025/02/11 daily challenge

stack approach
'''


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m, n = len(s), len(part)
        stack = []

        for i, c in enumerate(s):
            stack.append(c)
            if len(stack) >= n:
                for j, t in enumerate(reversed(part), start=1):
                    if stack[-j] != t:
                        break
                else:
                    # part matched, remove it
                    for _ in range(n):
                        stack.pop()

        return ''.join(stack)

