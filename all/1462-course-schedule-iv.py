'''
2025/01/27 daily challenge

topological sort approach
'''


import collections


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = collections.defaultdict(list)
        # deps[b] = {a} means course a is a prerequisite of course b.
        deps = [set() for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            g[a].append(b)
            deps[b].add(a)
            indegrees[b] += 1

        q = collections.deque([i for i, v in enumerate(indegrees) if v == 0])
        while q:
            node = q.popleft()
            for next_course in g[node]:
                deps[next_course].update(deps[node])
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    q.append(next_course)

        return [u in deps[v] for u, v in queries]

