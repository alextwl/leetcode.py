'''
2026/04/09 daily challenge

square root decomposition + multiplicative difference array + optimized 1/v approach

learnt from official editorial:
https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/editorial/#approach-square-root-decomposition--difference-array

same to problem 3653 with larger input
'''


import collections


MOD = 1_000_000_007


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        root = int(n ** 0.5 + 1e-7)

        # convert queries to key=(k, remainder) -> (multiplicand start, end, v)
        qd = collections.defaultdict(lambda: collections.defaultdict(list))
        for l, r, k, v in queries:
            if k <= root:
                start, rem = divmod(l, k)
                end = (r - rem) // k
                qd[k][rem].append((start, end, v))
            else:
                # in this category,
                # each query accesses at most (n / k) <= root elements,
                # brute force is acceptable.
                # time=O((n**0.5)q)
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % MOD

        # multiplier array
        muls = [1] * n
        for k, rem_dict in qd.items():
            for rem, q_list in rem_dict.items():
                m = ((n - rem) + k - 1) // k  # ceiling
                # multiplicative difference array
                diff = [1] * (m + 1)
                for start, end, v in q_list:
                    # apply multiplier v at start
                    diff[start] = diff[start] * v % MOD
                    # we need to cancel v after end,
                    # apply an inverse of v at (end + 1)
                    end_next = end + 1
                    if end_next < len(diff):
                        # use fermat's little theorem +
                        # modular multiplicative inverse +
                        # transitivity of modular arithmetic
                        # to prevent from doing 1/v directly.
                        #
                        # equivalent to diff[end_next] * (1 / v) % MOD
                        diff[end_next] = diff[end_next] * pow(v, MOD-2, MOD) % MOD

                # apply diffs to multiplier array
                val = 1
                for i, dv in enumerate(diff):
                    val = val * dv % MOD
                    idx = rem + i * k  # convert to nums' index
                    if idx < n:
                        muls[idx] = muls[idx] * val % MOD

        # calculate XOR ans
        ans = 0
        for num, mul in zip(nums, muls):
            ans ^= num * mul % MOD
        return ans

