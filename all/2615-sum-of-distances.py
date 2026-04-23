'''
2026/04/23 daily challenge

two-way prefix sums approach
'''


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        prevs = dict()
        cnts = dict()
        psum = dict()

        # build prefix sums
        for i, v in enumerate(nums):
            if v in prevs:
                psum[v] += (i - prevs[v]) * cnts[v]
                cnts[v] += 1
            else:
                psum[v] = 0
                cnts[v] = 1
            prevs[v] = i
            arr[i] = psum[v]

        # add suffix sums
        for i in range(n - 1, -1, -1):
            v = nums[i]
            if prevs[v] > i:
                psum[v] += (prevs[v] - i) * cnts[v]
                cnts[v] += 1
            else:
                psum[v] = 0
                cnts[v] = 1
            prevs[v] = i
            arr[i] += psum[v]

        return arr

