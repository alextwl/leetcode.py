'''
sorting + binary search approach
'''


import bisect


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = [(end, start, i) for i, (start, end) in enumerate(intervals)]
        arr.sort(reverse=True)
        ans = [-1] * len(intervals)

        ss = []  # sorted list: [(start, i), ...]
        # proceed from intervals with later end time
        for end, start, i in arr:
            # corner case: the problem also indicates that
            # the right interval may equal the current interval.
            if start == end:
                ans[i] = i
            else:
                j = bisect.bisect_left(ss, end, key=lambda x: x[0])
                if j < len(ss):
                    ans[i] = ss[j][1]

            bisect.insort(ss, (start, i))

        return ans

