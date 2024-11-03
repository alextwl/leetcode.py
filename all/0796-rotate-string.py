'''
2024/11/03 daily challenge

brute force approach
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i, c in enumerate(s):
            if c == goal[0] and (s[i:] + s[:i]) == goal:
                return True
        return False


'''
finding goal in the doubled string approach
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s * 2)


'''
Knuth-Morris-Pratt (KMP) algorithm approach

because the official solution included it...
'''


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(goal)
        if len(s) != n:
            return False

        # build Longest Prefix Suffix (LPS) array
        lps = [0] * n
        l = 0
        i = 1
        while i < n:
            if goal[i] == goal[l]:
                # char matched, increment the length and assign to lps
                l += 1
                lps[i] = l
                i += 1
            elif l > 0:
                # char mismatch, fallback to prev lps
                l = lps[l - 1]
            else:
                # char mismatch and length is zero, zero the lps and goto next char
                lps[i] = 0
                i += 1

        # do KMP search
        src = s * 2
        m = len(src)
        i = j = 0  # src's index, goal's index

        while i < m:
            if src[i] == goal[j]:
                # char matched
                i += 1
                j += 1
                if j == n:
                    return True
            elif j > 0:
                # char mismatch, fallback to prev lps
                j = lps[j - 1]
            else:
                # char mismatch and length is zero
                i += 1

        return False

