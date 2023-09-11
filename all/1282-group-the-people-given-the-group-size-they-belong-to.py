'''
2023/09/11 daily challenge

hash by group size
'''

import collections


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        # pools of groups to be formed.
        group_by_size = collections.defaultdict(list)
        
        for i, gsize in enumerate(groupSizes):
            group_by_size[gsize].append(i)
            if len(group_by_size[gsize]) == gsize:
                # group is full, ship it.
                ans.append(group_by_size[gsize])
                group_by_size[gsize] = list()

        return ans

