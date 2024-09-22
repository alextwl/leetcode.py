'''
2024/09/22 daily challenge

prefix tree approach

learnt from official solution:
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/solution/
'''


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(start, end):
            # count numbers between [start, end)
            cnt = 0
            while start <= n:
                cnt += min(end, n + 1) - start
                start *= 10
                end *= 10
            return cnt

        curr = 1
        k -= 1

        while k > 0:
            steps = count(curr, curr + 1)
            if steps <= k:
                # the target is in the current level
                curr += 1
                k -= steps
            else:
                # move to the next level and count only curr itself.
                curr *= 10
                k -= 1

        return curr

