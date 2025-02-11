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


'''
stack + Knuth-Morris-Pratt (KMP) approach
'''


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m, n = len(s), len(part)

        # build longest prefix suffix for input part
        lps = [0] * n

        i = 0  # left pointer is also a length of prefix
        j = 1  # right (current) pointer, must start from 1
        # kmp algorithm
        while j < n:
            if part[j] == part[i]:
                # char matched
                i += 1
                lps[j] = i
                j += 1
            elif i != 0:
                # char mismatch and not at the start
                # back to the previous lps
                i = lps[i - 1]
            else:
                # char mismatch and no previous lps available
                lps[j] = 0
                j += 1
        
        # traverse input string
        stack = []
        s_matching_indices = [0] * (m + 1)
        i = 0  # s index
        j = 0  # part index
        while i < m:
            c = s[i]
            stack.append(c)

            if c == part[j]:
                s_matching_indices[len(stack)] = j + 1
                j += 1

                if j == n:
                    # part matched, remove it from stack
                    for _ in range(n):
                        stack.pop()
                    # reset for next match
                    if stack:
                        j = s_matching_indices[len(stack)]
                    else:
                        j = 0
            else:
                # char mismatch
                if j != 0:
                    # backtrack by lps
                    i -= 1
                    j = lps[j - 1]
                    stack.pop()
                else:
                    # no previous lps available, reset
                    s_matching_indices[len(stack)] = 0
            i += 1
        return ''.join(stack)

