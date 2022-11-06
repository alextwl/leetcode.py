'''
2022/08/09 daily challenge

dynamic programming ver learnt from official solution
'''
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        # sort arr first, the largest value is also the largest root.
        # all existed children should be smaller than any root.
        arr.sort()
        # every value in arr is a valid root
        # for at least 1 tree which contains root only.
        dp = [1] * len(arr)
        val2idx = {v: i for i, v in enumerate(arr)}
        
        for rootidx, rootval in enumerate(arr):
            for leftidx in range(rootidx):
                # assume arr[leftidx] is always left child
                # right child maybe exist only if root was divisible by left
                if rootval % arr[leftidx] == 0:
                    # check if right child existed in arr (root = left * right)
                    rightval = rootval / arr[leftidx]
                    if rightval in val2idx:
                        # right child found, root dp contains all trees from left & right children
                        dp[rootidx] += dp[leftidx] * dp[val2idx[rightval]]
                        dp[rootidx] %= MOD

        return sum(dp) % MOD
