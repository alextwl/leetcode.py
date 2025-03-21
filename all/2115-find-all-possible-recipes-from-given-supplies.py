'''
2025/03/21 daily challenge

topological sort approach

convert the input to a directed graph,
the traversal starts from only supplies,
and visit recipes only after all its ingredients/dependent recipes visited.
'''


import collections


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = dict()
        g = collections.defaultdict(list)

        for r, ig in zip(recipes, ingredients):
            indegree[r] = len(ig)
            for v in ig:
                g[v].append(r)

        ans = []
        q = collections.deque(supplies)
        while q:
            v = q.popleft()  # an ingredient supplied (or a creatable recipe)
            for r in g[v]:
                indegree[r] -= 1
                if indegree[r] == 0:
                    q.append(r)
                    ans.append(r)

        return ans

