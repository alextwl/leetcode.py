'''
2026/03/13 daily challenge

binary answer + quadratic formula approach

binary search the minimum num of secs to make mountain height zero.

learnt from official editorial:
https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/editorial/#approach-binary-answer
'''


EPSILON = 1e-7


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        max_worker_time = max(workerTimes)

        ans = 0
        # binary search the second
        left = 0
        right = max_worker_time * (mountainHeight * (mountainHeight + 1)) // 2
        while left <= right:
            mid = (left + right) // 2
            # verify if mid sec could reduce the mountain height to zero
            reduced = 0
            # note the workers work simultaneously,
            # we need to find how much height (k) reduced by each worker.
            #
            # workerTimes[i] * (k*(k+1)//2) <= mid
            #
            # remainder of secs is discarded by floor because it's insufficient
            # to reduce mountain height one more unit for the current worker.
            # so we have the inequality:
            #
            # k*(k+1)//2 <= mid // workerTimes[i]
            for t in workerTimes:
                w = mid // t  # floor(mid / workerTimes[i])
                # solve (k*(k+1)//2 <= work) by quadratic formula
                k = int((-1 + ((1 + w * 8) ** 0.5)) / 2 + EPSILON)
                reduced += k
                if reduced >= mountainHeight:
                    break

            if reduced >= mountainHeight:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

