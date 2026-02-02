'''
2026/02/02 daily challenge

ordered list + sliding window approach
'''


import bisect


class Window:
    def __init__(self, size):
        self.size = size
        # sorted lists
        self.inside = []  # (k-2) smallest elements in non-decreasing order
        self.outside = []  # other elements in dist in non-increasing order
        self.sum_val = 0

    def add(self, val):
        if len(self.inside) < self.size:
            bisect.insort(self.inside, val)
            self.sum_val += val
        else:
            if val < self.inside[-1]:
                out = self.inside.pop()
                bisect.insort(self.outside, -out)
                bisect.insort(self.inside, val)
                self.sum_val += val - out
            else:
                bisect.insort(self.outside, -val)

    def remove(self, val):
        if self.inside and val <= self.inside[-1]:
            del self.inside[bisect.bisect_left(self.inside, val)]
            self.sum_val -= val

            if self.outside:
                self.inside.append(-self.outside.pop())
                self.sum_val += self.inside[-1]
        else:
            del self.outside[bisect.bisect_left(self.outside, -val)]


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # build a sliding window
        win = Window(k - 2)
        win.inside = nums[1:k-1]
        win.inside.sort()
        win.sum_val = sum(win.inside)
        # base case: ((k-2)-smallest in nums[1:k-1]) +
        #            (nums[k - 1] as the cost of last subarray)
        # note the cost of first subarray is not yet included.
        ans = win.sum_val + nums[k - 1]

        # index of the last element to be out of sliding window
        j = k - dist - 1
        # try from nums[k] to nums[n - 1] as the cost of last subarray
        for i in range(k, len(nums)):
            if j > 0:
                win.remove(nums[j])
            win.add(nums[i - 1])

            ans = min(ans, win.sum_val + nums[i])
            j += 1

        return nums[0] + ans

