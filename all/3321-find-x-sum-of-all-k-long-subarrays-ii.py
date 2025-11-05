'''
2025/11/05 daily challenge

binary search + sliding window approach

maintain xsum and top-x window gradually during addition/removal.

Runtime=2017ms, Beats 85.71%
'''


import bisect
import collections


class Subarray:
    def __init__(self, x):
        self.x = x
        self.freq = collections.defaultdict(int)
        self.slist = list()  # (frequency, key value)
        self.xsum = 0

    def add(self, v):
        # flag indicating removing one tuple from Top-x occured
        removal = False
        if self.freq[v]:
            # remove old tuple
            t = (self.freq[v], v)
            i = bisect.bisect_left(self.slist, t)
            if len(self.slist) - i <= self.x:
                self.xsum -= self.freq[v] * v
                removal = True
            self.slist.pop(i)

        # insert new tuple
        self.freq[v] += 1
        t = (self.freq[v], v)
        i = bisect.bisect_left(self.slist, t)
        self.slist.insert(i, t)
        if len(self.slist) - i <= self.x:
            self.xsum += self.freq[v] * v
            if not removal and len(self.slist) > self.x:
                # Top-x window is full, removing top-(x+1) from xsum
                self.xsum -= int.__mul__(*self.slist[-self.x-1])
        elif removal and len(self.slist) >= self.x:
            # fill a vacancy in top-x window
            self.xsum += int.__mul__(*self.slist[-self.x])

    def delete(self, v):
        # flag indicating removing one tuple from Top-x occured
        removal = False
        # remove old tuple
        t = (self.freq[v], v)
        i = bisect.bisect_left(self.slist, t)
        if len(self.slist) - i <= self.x:
            self.xsum -= self.freq[v] * v
            removal = True
        self.slist.pop(i)

        # insert new tuple
        self.freq[v] -= 1
        if self.freq[v]:
            t = (self.freq[v], v)
            i = bisect.bisect_left(self.slist, t)
            self.slist.insert(i, t)
            if len(self.slist) - i <= self.x:
                self.xsum += self.freq[v] * v
                if not removal and len(self.slist) > self.x:
                    # Top-x window is full, removing top-(x+1) from xsum
                    self.xsum -= int.__mul__(*self.slist[-self.x-1])
                return
        if removal and len(self.slist) >= self.x:
            # fill a vacancy in top-x window
            self.xsum += int.__mul__(*self.slist[-self.x])

    def rebuild_xsum(self):
        self.xsum = sum(fq * v for fq, v in self.slist[-self.x:])
        return self.xsum
    
    def get_xsum(self):
        return self.xsum


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # init with the beginning length-k window
        sub = Subarray(x)
        init_ctr = collections.Counter(nums[:k])
        for v, fq in init_ctr.items():
            sub.freq[v] = fq
            sub.slist.append((fq, v))
        sub.slist.sort()
        ans = [sub.rebuild_xsum()]

        # slide thw window
        left = 0
        for right in range(k, len(nums)):
            if nums[left] != nums[right]:
                sub.delete(nums[left])
                sub.add(nums[right])
            ans.append(sub.get_xsum())
            left += 1

        return ans

