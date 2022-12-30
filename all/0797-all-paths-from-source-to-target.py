'''
2022/12/30 daily challenge

depth first search approach
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = []  # answer
        terminal = len(graph) - 1  # end node: n-1

        def dfs(src, path: List[int]):
            path.append(src)
            if src == terminal:
                all_paths.append(path.copy())
            else:
                for child in graph[src]:
                    dfs(child, path)
            path.pop()
        
        dfs(0, [])  # start from 0

        return all_paths

