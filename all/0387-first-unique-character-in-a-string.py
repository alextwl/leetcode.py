'''
2022/08/16 daily challenge
2024/02/05 daily challenge

hash & set approach
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        first_index = dict()
        repeated = set()
        
        for i, c in enumerate(s):
            if c in first_index:
                repeated.add(c)
                del first_index[c]
            elif c not in repeated:
                first_index[c] = i

        return min(first_index.values(), default=-1)

