'''
2023/11/20 daily challenge

counter approach
'''


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        assorts = {'M': 0, 'P': 0, 'G': 0}  # the count of garbage
        last_idx = {'M': 0, 'P': 0, 'G': 0}  # the last index of garbage seen by type

        for idx, trash in enumerate(garbage):
            for v in "MPG":
                if w := trash.count(v):
                    assorts[v] += w
                    last_idx[v] = idx

        # count the number of minutes picking up garbage
        ans = sum(assorts.values())
        # count the number of minutes traveling to the terminal
        for term in last_idx.values():
            if term:
                ans += sum(travel[:term])

        return ans

