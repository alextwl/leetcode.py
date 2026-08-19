'''
2026/08/19 daily challenge

subset matching approach
'''


import collections


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        occupied = collections.defaultdict(list)
        for i, j in reservedSeats:
            occupied[i].append(j)

        valid_groups = 0
        for used_seats in map(set, occupied.values()):
            curr_groups = 0
            if not({2, 3, 4, 5} & used_seats):
                curr_groups = 1
            if not({6, 7, 8, 9} & used_seats):
                curr_groups += 1
            if curr_groups == 0 and not({4, 5, 6, 7} & used_seats):
                curr_groups = 1
            valid_groups += curr_groups

        # unused rows can provide seats for 2 groups.
        return valid_groups + (n - len(occupied)) * 2

