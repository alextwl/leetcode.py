'''
2025/02/12 daily challenge

hashmap approach

maintain the maximum value of nums by sum of digits as its key.
'''


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dsum_max = dict()  # key=sum of digits, value=max value of nums

        max_val = -1  # init with no answer val=-1
        for v in nums:
            dsum = sum(int(dig) for dig in str(v))
            if dsum in dsum_max:
                max_val = max(max_val, dsum_max[dsum] + v)
            dsum_max[dsum] = max(dsum_max.get(dsum, 0), v)

        return max_val


'''
min heap approach

keep two largest nums of each sum of digits by heap,
and then maximize the sum of pairs.

note all values of each pair share the same sum of digits.
'''


import collections
import heapq


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_dsum(int_val):
            ret = 0
            while int_val:
                int_val, rem = divmod(int_val, 10)
                ret += rem
            return ret

        dsum_h = collections.defaultdict(list)  # key=sum of digits, value=min heap of original values

        for v in nums:
            dsum = get_dsum(v)
            if len(dsum_h[dsum]) == 2:
                if dsum_h[dsum][0] < v:
                    heapq.heapreplace(dsum_h[dsum], v)
            else:
                heapq.heappush(dsum_h[dsum], v)

        return max((sum(h) for h in dsum_h.values() if len(h) == 2), default=-1)

