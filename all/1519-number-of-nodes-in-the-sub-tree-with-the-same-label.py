'''
2023/01/12 daily challenge

recursive depth first search approach
'''

import string


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # build tree
        vv = [set() for _ in range(n)]
        for a, b in edges:
            vv[a].add(b)
            vv[b].add(a)

        ans = [0] * n
        lblcounts = {c: 0 for c in string.ascii_lowercase}

        def dfs(val, parent):
            '''
            :param val: the value of the input node
            :param parent: the value of the input node's parent
            '''
            # obtain the current node's label
            lbl = labels[val]
            # save label counted from other branches.
            other_lblcount = lblcounts[lbl]
            # visit the node
            lblcounts[lbl] += 1

            # traverse the subtree
            for child in vv[val] - {parent}:
                dfs(child, val)

            # calculate the answer of the current node's label excluding other branches' counts.
            ans[val] = lblcounts[lbl] - other_lblcount

        # traverse from node 0.
        dfs(0, None)

        return ans

