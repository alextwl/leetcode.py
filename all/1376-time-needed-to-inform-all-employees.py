'''
2023/06/03 daily challenge

depth first search approach
'''


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # build uni-directional graph[mgr] = {his direct subordinates}
        graph = [set() for _ in range(n)]
        for i, mgr in enumerate(manager):
            if mgr >= 0:
                graph[mgr].add(i)

        ans = 0
        # DFS
        stack = [(headID, 0)]
        while(stack):
            staff_id, total_time = stack.pop()
            total_time += informTime[staff_id]
            ans = max(ans, total_time)

            # inform his direct subordinates
            for i in graph[staff_id]:
                stack.append((i, total_time))

        return ans

