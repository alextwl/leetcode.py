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

