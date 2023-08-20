'''
2023/08/20 daily challenge

topological sorting approach

learnt from official solution:
https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/solution/
'''


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        '''
        an item without a group is deemed to be within an independent group,
        assign each non-group item to a new group id.
        '''
        next_gid = m
        for item, gid in enumerate(group):
            if gid == -1:
                group[item] = next_gid
                next_gid += 1

        '''
        convert items to a directed acyclic graph.
        
        item_graph[i] = [j, ...]  # i -> [j, ...]
        '''
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n  # incoming edge counter for detecting cycle

        '''
        convert groups to a directed acyclic graph.
        '''
        group_graph = [[] for _ in range(next_gid)]  # including those new groups appended after input.
        group_indegree = [0] * next_gid
        
        '''
        iterate all items and build graph by dependencies
        '''
        for curr_item in range(n):
            for prereq_item in beforeItems[curr_item]:
                '''
                build item graph by dependency.
                prereq_item -> curr_item
                '''
                item_graph[prereq_item].append(curr_item)
                item_indegree[curr_item] += 1

                '''
                if they were different groups, we also need to create group dependency.
                
                prereq_item's group -> curr_item's group.
                '''
                curr_gid, prereq_gid = group[curr_item], group[prereq_item]
                if prereq_gid != curr_gid:
                    group_graph[prereq_gid].append(curr_gid)
                    group_indegree[curr_gid] += 1

        def topoSort(graph, indegree):
            '''
            Run topological sorting to detect cycle by Kahn's algorithm.
            '''
            # a list will contain sorted elements
            L = []
            # a list containing nodes without incoming edge. also a stack.
            S = [i for i in range(len(graph)) if indegree[i] == 0]

            while(S):
                node = S.pop()

                '''
                the node has no more unvisited incoming edge,
                feel free to append it to the sorted list.
                '''
                L.append(node)

                '''
                traverse its neighbors.
                '''
                for child in graph[node]:
                    indegree[child] -= 1
                    '''
                    the node has no more unvisited incoming edge,
                    safe to add it to the stack for deeper traversal.
                    '''
                    if indegree[child] == 0:
                        S.append(child)

            if len(L) < len(graph):
                '''
                there are nodes whose indegree is not zero,
                cycle detected.
                '''
                return []

            # the graph is a valid DAG and we can return its sorted list.
            return L

        # do topological sorting and detect cycles
        item_order = topoSort(item_graph, item_indegree)
        group_order = topoSort(group_graph, group_indegree)

        if not item_order or not group_order:
            '''
            cycle detected, we cannot find a valid sorted item list.
            '''
            return []

        '''
        build sorted item list by group.
        '''
        sorted_group_items = [[] for _ in range(next_gid)]
        for item in item_order:
            sorted_group_items[group[item]].append(item)

        '''
        concatenate all sorted item list by group order.
        '''
        ans = []
        for gid in group_order:
            ans += sorted_group_items[gid]

        return ans

