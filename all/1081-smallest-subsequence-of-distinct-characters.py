'''
2026/07/19 daily challenge

monotonic stack + bitmasking + greedy method approach

similar to problem 316.
'''


ASCII_A = ord('a')
FULL_MASK = (1 << 26) - 1


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen = 0  # bitmask of seen alphabets

        # 0-indexed counter of alphabets
        ctr = [0] * 26
        for v in map(ord, s):
            ctr[v - ASCII_A] += 1

        stack = []  # non-decreasing monotonic stack
        for c in s:
            i = ord(c) - ASCII_A

            if not(seen & (1 << i)):
                # delete previous chars greater than current char
                # until a smaller one encountered.
                while stack and stack[-1] > c:
                    top_i = ord(stack[-1]) - ASCII_A
                    if ctr[top_i]:
                        # unset top_i bit
                        seen = seen & (FULL_MASK - (1 << top_i))
                        stack.pop()
                    else:
                        break
                seen |= 1 << i
                stack.append(c)
            ctr[i] -= 1

        return ''.join(stack)

