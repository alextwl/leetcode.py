'''
2025/07/24 daily challenge

depth first search + XOR approach

learnt from official editorial 2:
https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/editorial/#approach-2-enumerate-based-on-dfs-order

calculate XOR for subtrees rooted at each node when doing DFS,
and then do O(n**2) search for each pairs of (u, v) with 3 scenarios.
'''


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        cnt = 0  # the time when visiting next node
        tree_xor = [0] * n  # tree_xor[i] = xor sum rooted at node i
        time_in = [0] * n  # time_in[i] = time when dfs visited node i
        time_out = [0] * n  # time_out[i] = time when dfs quitted node i

        g = [list() for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        def dfs(x, parent):
            nonlocal cnt
            time_in[x] = cnt
            cnt += 1

            tree_xor[x] = nums[x]
            for y in g[x]:
                if y == parent:
                    continue
                dfs(y, x)
                tree_xor[x] ^= tree_xor[y]
            time_out[x] = cnt
        
        dfs(0, None)

        get_score = lambda a, b, c: max(a, b, c) - min(a, b, c)
        ans = float('inf')
        for u in range(1, n):
            for v in range(u + 1, n):
                if time_in[v] > time_in[u] and time_in[v] < time_out[u]:
                    # u is an ancestor of v
                    # node 0 -> ... (remove) -> u -> ... (remove) -> v -> ...
                    # ^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^
                    #         part 1                  part 2          part 3
                    ans = min(ans,
                              get_score(tree_xor[0] ^ tree_xor[u],
                                        tree_xor[u] ^ tree_xor[v],
                                        tree_xor[v])
                             )
                elif time_in[u] > time_in[v] and time_in[u] < time_out[v]:
                    # v is an ancestor of u
                    # node 0 -> ... (remove) -> v -> ... (remove) -> u -> ...
                    # ^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^
                    #         part 1                  part 2          part 3
                    ans = min(ans,
                              get_score(tree_xor[0] ^ tree_xor[v],
                                        tree_xor[u] ^ tree_xor[v],
                                        tree_xor[u])
                             )
                else:
                    # u & v are not ancestor of each other,
                    # but node 0 is their ancestor.
                    #
                    # remove a upper level edge for both u & v.
                    #
                    # node 0 --+--> ... (remove) -> u -> ...
                    #          |                   ^^^^^^^^^^
                    #          |                     part 2
                    #          +--> ... (remove) -> v -> ...
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^  ^^^^^^^^^^
                    #            part 1              part 3
                    ans = min(ans,
                              get_score(tree_xor[0] ^ tree_xor[u] ^ tree_xor[v],
                                        tree_xor[u],
                                        tree_xor[v])
                             )
        return ans

