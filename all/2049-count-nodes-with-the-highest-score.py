'''
depth first search approach

similar to problem 1339.
'''


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        max_score = 0
        ans = 0

        # convert parents to g[parent] = [child node, ...]
        g = [list() for _ in range(n)]
        for i, v in enumerate(parents):
            if v >= 0:
                g[v].append(i)

        def dfs(idx):
            nonlocal n, g, max_score, ans

            sub_counts = 0
            product = 1
            for sub in g[idx]:
                cnt = dfs(sub)
                product = product * cnt
                sub_counts += cnt

            # size of idx's parent as a subtree after idx node removed
            upper_size = n - sub_counts - 1
            if upper_size > 0:
                product = product * upper_size

            # the question actually asks for the number of **cases** that
            # have the highest score.
            if product > max_score:
                max_score = product
                ans = 1
            elif product == max_score:
                ans += 1

            return sub_counts + 1

        dfs(0)
        return ans

