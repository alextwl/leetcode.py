'''
2024/06/27 daily challenge

set approach
'''


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()

        for u, v in edges:
            if u in seen:
                return u
            seen.add(u)
            if v in seen:
                return v
            seen.add(v)

        return -1  # undefined

