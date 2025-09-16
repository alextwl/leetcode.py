'''
stack approach
'''


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        curr = s[0]
        repeat = 0

        for c in s:
            if c == curr:
                repeat += 1
                if repeat == k:
                    # reset counter to remove k adjacent duplicates.
                    # retrieve last letter or duplicates from stack.
                    curr = stack[-1] if stack else None
                    repeat = 0
                    while stack and stack[-1] == curr:
                        repeat += 1
                        stack.pop()
            else:
                stack.extend([curr] * repeat)
                curr = c
                repeat = 1

        stack.extend([curr] * repeat)
        return ''.join(stack)

