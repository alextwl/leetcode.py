'''
2025/10/19 daily challenge

depth first search approach

learnt from @zarathustralala's solution:
https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/solutions/7284462/it-s-a-graph-problem-yessir-let-s-draw-it-cycle-visualization-and-dfs

generate all possible permutations and get the smallest.
'''


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        ADD = {str(i): str((i + a) % 10) for i in range(10)}

        def op1_add(s):
            # add a to all odd indices
            return ''.join(ADD[c] if i & 1 else c for i, c in enumerate(s))

        def op2_rotate(s):
            return s[n - b:] + s[:n - b]

        visited = set()

        def dfs(s):
            if s in visited:
                return
            visited.add(s)
            dfs(op1_add(s))
            dfs(op2_rotate(s))

        dfs(s)
        return min(visited)

