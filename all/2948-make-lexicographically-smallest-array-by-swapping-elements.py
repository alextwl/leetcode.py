'''
2025/01/25 daily challenge
2026/08/29 daily challenge

sorting + grouping approach

learnt from official editorial:
https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/editorial/

property: if a can swap with b and b can swap with c,
then a can eventually be swapped with c.

intuition: we split the sorted array into one or multiple groups,
and any elements in the same group can swap freely.

assign group numbers to each element (position) in the original array,
and then rebuild the array by group.
in the rearrangement of each position of original array,
the smallest unused element of its group is
popped and inserted to the original array.
'''


import collections


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted(nums)

        current_group = 0
        num2grp = {}
        num2grp[arr[0]] = current_group

        grp2list = collections.defaultdict(list)
        grp2list[current_group] = [arr[0]]

        for i in range(1, len(nums)):
            if abs(arr[i] - arr[i-1]) > limit:
                # add new group if the diff exceeded the limit
                current_group += 1
            num2grp[arr[i]] = current_group
            grp2list[current_group].append(arr[i])

        for i in range(len(nums)):
            v = nums[i]
            nums[i] = grp2list[num2grp[v]].pop(0)

        return nums


'''
yet another sorting + component list (simplified disjoint set union) approach
'''


import itertools


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # num value to its belonging component list in non-increasing order
        v2comp = dict()
        # sort nums in non-increasing order
        dec = sorted(nums, reverse=True)
        # initial component
        curr_comp = [dec[0]]
        v2comp[dec[0]] = curr_comp

        for prev, curr in itertools.pairwise(dec):
            # check if adjacent nodes were in the same component or not
            if prev - curr > limit:
                # cannot swap curr with prev, new component for curr
                curr_comp = []
            curr_comp.append(curr)
            v2comp[curr] = curr_comp

        ans = [v2comp[v].pop() for v in nums]
        return ans

