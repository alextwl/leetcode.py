'''
2025/05/01 daily challenge

binary search + greedy method approach

learnt from official editorial:
https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/editorial/
'''


import bisect


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def validate(mid):
            pill_quota = pills
            q = workers[-mid:]

            for i in range(mid - 1, -1, -1):
                if q[-1] >= tasks[i]:
                    q.pop()
                else:
                    if pill_quota == 0:
                        return False
                    # try to use a pill for the minimum element >= (task - strength)
                    j = bisect.bisect_left(q, tasks[i] - strength)
                    if j == len(q):
                        # the worker cannot complete any task with pill.
                        return False
                    pill_quota -= 1
                    q.pop(j)
            return True
        
        l, r = 1, min(len(tasks), len(workers))
        ans = 0
        while l <= r:
            mid = (l + r) >> 1
            if validate(mid):
                ans = mid
                # try to extend the upper bound
                l = mid + 1
            else:
                r = mid - 1
        return ans

