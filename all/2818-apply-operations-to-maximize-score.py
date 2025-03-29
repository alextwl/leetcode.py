'''
2025/03/29 daily challenge

monotonic decreasing stack + max heap approach

learnt from official editorial 1:
https://leetcode.com/problems/apply-operations-to-maximize-score/editorial/#approach-1-monotonic-stack--priority-queue
'''


import heapq


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # build a list of prime scores of nums
        prime_scores = [0] * n
        for i, v in enumerate(nums):
            # iterate factors in [2, square root of v] range
            for factor in range(2, int(v ** 0.5) + 1):
                if v % factor == 0:
                    prime_scores[i] += 1
                    while v % factor == 0:
                        # remove same factors from current value
                        v //= factor
            if v >= 2:
                # if the last quotient was not 1, the original value is a prime.
                prime_scores[i] += 1

        # build infos of the relative dominants for later subarray selections.
        next_dom = [n] * n  # next dominants of nums
        prev_dom = [-1] * n  # previous dominants of nums

        # monotonic stack in prime score decreasing order
        stack = []  # indices of prime scores
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                next_dom[stack.pop()] = i
            if stack:
                prev_dom[i] = stack[-1]
            stack.append(i)
        
        # subarray_counts[i] = the number of subarrays with dominant element nums[i]
        subarray_counts = [(x - i) * (i - y) for i, (x, y) in enumerate(zip(next_dom, prev_dom))]

        # max heap (-v, i)
        h = []
        for i, v in enumerate(nums):
            heapq.heappush(h, (-v, i))
        
        # power() helper with 10**9-7 modulo
        def power_mod(base, exp):
            ret = 1
            while exp:
                if exp & 1:
                    ret = (ret * base) % 1_000_000_007
                base = (base * base) % 1_000_000_007
                exp //= 2
            return ret
        
        ans = 1
        # count scores
        while k > 0:
            v, i = heapq.heappop(h)
            v = -v

            ops = min(k, subarray_counts[i])
            ans = (ans * power_mod(v, ops)) % 1_000_000_007
            k -= ops
        return ans

