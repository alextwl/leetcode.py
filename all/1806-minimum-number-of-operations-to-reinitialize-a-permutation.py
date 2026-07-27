'''
brute force approach
'''


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        prev = list(range(n))
        curr = [prev[n//2 + (i-1)//2] if i & 1 else prev[i//2] for i in range(n)]

        ops = 1
        while curr != perm:
            prev, curr = curr, prev
            for i in range(n):
                curr[i] = prev[n//2 + (i-1)//2] if i & 1 else prev[i//2]
            ops += 1

        return ops


'''
track the movement of perm[1] reversely
'''


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1

        ops = 1
        i = 2  # the first operation done, init from i = 1, and then i = i * 2
        # reverse the operation, track where perm[i] is assigned to.
        while i != 1:
            if i * 2 < n:
                i = i * 2
            else:
                i = (i - n // 2) * 2 + 1
            ops += 1

        return ops

