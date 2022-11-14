'''
2022/11/14 daily challenge

the depth first search approach is similar to problem 200 number of islands.

treat stones **sharing the same row or the same column** as an island.

for each island, we can remove stones until the island has at most one stone,
so the number of islands is also the number of the least stones we cannot remove.
'''

import collections


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(coords, shares, i, j):
            # visit the coordinate.
            coords.discard((i, j))
            '''
            in problem 200 an island is formed by
            connecting adjacent lands horizontally or vertically.
            
            here we search all stones sharing either the same row or column.
            '''
            # find any (i, *) sharing the same row.
            for col in shares[i]:
                if (i, col) in coords:
                    dfs(coords, shares, i, col)
            # find any (*, j) sharing the same column.
            for row in shares[~j]:
                if (row, j) in coords:
                    dfs(coords, shares, row, j)
        
        # convert stones to sets for easier searching
        coords = {(i, j) for i, j in stones}
        # island counter.
        islands = 0
        '''
        a union coordinate index with row + column keys. col key is bitwise inverted.
        shares[row] = [cols]
        shares[~col] = [rows]
        '''
        shares = collections.defaultdict(list)
        for i, j in coords:
            shares[i].append(j)
            shares[~j].append(i)
        
        for i, j in stones:
            '''
            if the stone was not yet visited, we can count it and start searching.
            '''
            if (i, j) in coords:
                dfs(coords, shares, i, j)
                islands += 1

        return len(stones) - islands

