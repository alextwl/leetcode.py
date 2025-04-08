'''
depth first search approach (exhaustive method)

learnt from official editorial 2:
https://leetcode.com/problems/pyramid-transition-matrix/editorial/
'''


import collections


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pat = collections.defaultdict(set)
        for a, b, c in allowed:
            pat[(a, b)].add(c)
        
        def build_row(curr_row, next_row):
            # inner DFS: build all possible combinations of next_row
            # if there's no matched pattern, it doesn't yield anything.
            i = len(next_row)
            if len(next_row) == len(curr_row) - 1:
                # next_row fully filled, yield its string.
                yield ''.join(next_row)
            else:
                # iterate all possible adjacent cells next to next_row[-1]
                for next_adj in pat[(curr_row[i], curr_row[i+1])]:
                    next_row.append(next_adj)
                    for next_row_str in build_row(curr_row, next_row):
                        yield next_row_str
                    next_row.pop()

        def dfs(curr_row):
            # DFS by row
            if len(curr_row) == 1:
                return True
            for next_row_str in build_row(curr_row, []):
                if dfs(next_row_str):
                    return True
            return False

        return dfs(bottom)


'''
simplified DFS (backtracking ver)

search from left to right, bottom to top.
'''


import collections


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pat = collections.defaultdict(list)
        for a, b, c in allowed:
            pat[(a, b)].append(c)

        invalids = set()

        def dfs(curr_row, next_row):
            next_row_str = ''.join(next_row)
            if next_row_str and next_row_str in invalids:
                return False

            i = len(next_row)
            if i == len(curr_row) - 1:
                if i == 1:
                    # top of pyramid reached
                    return True
                # continue building the next row
                return dfs(next_row, [])

            # search adjacent cells
            for next_adj in pat[(curr_row[i], curr_row[i+1])]:
                if next_row and (next_row[-1], next_adj) not in pat:
                    # don't yield if we've known (last cell, next_adj) is invalid
                    continue
                next_row.append(next_adj)
                if dfs(curr_row, next_row):
                    return True
                next_row.pop()

            invalids.add(next_row_str)
            return False

        return dfs(bottom, [])

