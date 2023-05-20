'''
2023/05/20 daily challenge

depth first search approach
'''

import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build bidirectional equation lookups
        lookup = collections.defaultdict(dict)  # lookup[a][b] = quotient of a / b
        graph = collections.defaultdict(set)
        for eq, quo in zip(equations, values):
            a, b = eq
            lookup[a][b] = quo
            if a not in lookup[b]:
                '''
                Ai / Bi = quo
                Ai = quo * Bi
                1 = quo * Bi / Ai
                1 / quo = Bi / Ai
                '''
                lookup[b][a] = 1.0 / quo
            
            graph[a].add(b)
            graph[b].add(a)
        
        def dfs(node: str, parent: str, target: str, path: List[str]) -> bool:
            '''
            :return: True if target found
            '''
            if node in path:
                # cycle found, stop it.
                return False
            # add node to path (visit the node)
            path.append(node)

            if node == target:
                # target found
                return True

            for child in graph[node] - {node}:
                if dfs(child, node, target, path):
                    return True

            # target not found, remove the node
            path.pop()
            return False

        # time to evaluate the queries
        ans = []
        for c, d in queries:
            if c == d:
                # shortcut to foo/foo
                if c in graph:
                    ans.append(1.0)
                else:
                    # note: foo/foo = -1.0 if foo is undefined as in Example 1.
                    ans.append(-1.0)
                continue
            '''
            find the equation path from c to d
            e.g.
            (c / a) * (a / b) * (b / d) = c / d
            then the list is [c, a, b, d].
            '''
            cd_equation = []
            if dfs(c, None, d, cd_equation):
                it = iter(cd_equation)
                next(it)  # the node c, discard it.
                prev_node = next(it)  # the node next to the beginning node c
                mult = lookup[c][prev_node]
                for next_node in it:
                    mult = mult * lookup[prev_node][next_node]
                    prev_node = next_node
                ans.append(mult)
            else:
                # answer not found
                ans.append(-1.0)

        return ans

