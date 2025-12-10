'''
2025/12/10 daily challenge

factorial approach

the sequence of computers after root can be rearranged,
because we can always use root key (j=0) to unlock all computers.
as long as there's no computer with complexity <= root's,
the number of permutations is (n - 1)!.

[1 selection becuase it's root, (n - 1) sels, (n - 2) sels, ..., 1 sel]
'''


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        it = enumerate(complexity)
        _, min_val = next(it)
        ans = 1
        for i, v in it:
            if v <= min_val:
                # the complexity of current computer is not higher than root's,
                # cannot unlock.
                return 0
            ans = (ans * i) % 1_000_000_007

        return ans

