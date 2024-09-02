'''
2024/09/02 daily challenge

prefix sum + binary search approach
'''


import bisect


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        running_sum = 0
        prefix_sums = []
        for v in chalk:
            running_sum += v
            prefix_sums.append(running_sum)

        k %= prefix_sums[-1]

        return bisect.bisect_right(prefix_sums, k)


'''
simulation approach

surprisingly a bit faster than prefix sum + binary search ver.
'''


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i, v in enumerate(chalk):
            if k < v:
                return i
            k -= v
        return 0  # undefined

