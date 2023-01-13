'''
2023/01/13 daily challenge

recursive depth first search approach
'''

import collections


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # build tree
        nodes = collections.defaultdict(set)
        for i, p in enumerate(parent):
            '''
            although the problem gave an undirected tree,
            since it's guaranteed no cycles and we are going to run DFS,
            we only need parent->child links.
            '''
            nodes[p].add(i)

        longest = 1  # the overall longest path length.

        def dfs(v):
            '''
            we are going to find if there're:

            (1) two subtrees that provide us 2 long path
                which can be concatenated with input v as overall longest path.

                subtree 1's longest <-> v <-> subtree 2's longest

            (2) or the result from (1) cannot beat the current overall longest.
                the overall longest remains.

            and then we always return the 1st longest path from subtree plus input v
            to reverse the possibility to find a more longer path which contains this path.

                path from other branch <-> v <-> subtree 1's longest
            '''
            nonlocal longest
            path1 = path2 = 0  # the 1st & 2nd longest length of pathes from subtrees

            for child in nodes[v]:
                childpath = dfs(child)  # always traverse child

                '''
                bypass adjacent node which can be a pair of the same char with input v.

                note: although we cannot bring adjacent nodes with the same char into the longest path,
                there may be a longest path in the subtrees without passing though the input v.

                thus we always traverse child no matter whether it has the same char with v or not.
                '''
                if s[v] == s[child]:
                    continue

                # update the 1st/2nd longest path from subtrees
                if childpath > path1:
                    path1, path2 = childpath, path1
                elif childpath > path2:
                    path2 = childpath

            # try to beat overall longest by path1 + v + path2
            longest = max(longest, path1 + 1 + path2)

            return path1 + 1

        # traverse from root
        dfs(0)

        return longest

