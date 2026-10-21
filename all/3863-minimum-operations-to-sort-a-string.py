'''
2026/10/21 daily challenge

sorting + condition checking approach
'''


class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0

        min_c = max_c = s[0]
        for c in s:
            if c < min_c:
                min_c = c
            if c > max_c:
                max_c = c

        if len(s) == 2 and s[0] != min_c:
            return -1

        ss = sorted(list(s))
        if ''.join(ss) == s:
            return 0
        if s[0] == min_c or s[-1] == max_c:
            return 1
        for c in s[1:-1]:
            if c == min_c or c == max_c:
                return 2
        # we have s[0] == max_c and s[-1] == min_c,
        # and we need 3 ops to get these elements sorted.
        # (1) sort s[:-1],
        # (2) sort s[1:],
        # (3) and sort s[:-1] again.
        return 3


'''
condition checking only (without actually sorting input s)
'''


class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0

        min_c = max_c = s[0]
        for c in s:
            if c < min_c:
                min_c = c
            if c > max_c:
                max_c = c

        if len(s) == 2 and s[0] != min_c:
            return -1

        # check whether s was already sorted or not.
        for a, b in zip(s, s[1:]):
            if a > b:
                break
        else:
            # s is already sorted.
            return 0

        if s[0] == min_c or s[-1] == max_c:
            return 1
        for c in s[1:-1]:
            if c == min_c or c == max_c:
                return 2
        # we have s[0] == max_c and s[-1] == min_c,
        # and we need 3 ops to get these elements sorted.
        # (1) sort s[:-1],
        # (2) sort s[1:],
        # (3) and sort s[:-1] again.
        return 3

