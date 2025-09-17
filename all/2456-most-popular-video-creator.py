'''
hashmap approach
'''


import collections


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        self.creator_id = dict()
        self.creator_views = collections.defaultdict(int)
        self.creator_max_views = collections.defaultdict(int)

        for c, i, v in zip(creators, ids, views):
            self.creator_views[c] += v
            if v > self.creator_max_views[c]:
                self.creator_id[c] = i
                self.creator_max_views[c] = v
            elif v == self.creator_max_views[c]:
                if c in self.creator_id:
                    self.creator_id[c] = min(self.creator_id[c], i)
                else:
                    self.creator_id[c] = i

        most_populars = []
        max_views = 0
        for c, v in self.creator_views.items():
            if v > max_views:
                most_populars = [c]
                max_views = v
            elif v == max_views:
                most_populars.append(c)

        return [[c, self.creator_id[c]] for c in most_populars]

