'''
2023/07/13 daily challenge

Kahn's algorithm + breadth first search approach

we can finish all courses if there's no cycle.
'''

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses  # the incoming indegree of course
        
        # build graph with edge: course -> prereq(s)
        g = collections.defaultdict(list)
        for course, prereq in prerequisites:
            g[course].append(prereq)
            indegree[prereq] += 1
        
        # BFS
        q = collections.deque()
        for i, incomings in enumerate(indegree):
            # start from zero-indegree courses
            if incomings == 0:
                q.append(i)
        while(q):
            course = q.popleft()
            for prereq in g[course]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)
        
        # we can finish all courses only if all courses' indegrees are zero.
        return not any(indegree)


'''
depth first search approach
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph with edge: course -> prereq(s)
        g = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            g[course].append(prereq)
        
        visitedCourses = set()
        tempCourses = set()
        
        def dfs(course):
            nonlocal g, visitedCourses, tempCourses

            if course in visitedCourses:
                # visited, no need to traverse further
                return True
            
            if course in tempCourses:
                # cycle found, we cannot finish all courses in the current travel.
                return False
            
            tempCourses.add(course)
            
            # search deeper courses
            for prereq in g[course]:
                if not dfs(prereq):
                    return False
            
            tempCourses.remove(course)
            visitedCourses.add(course)
            return True
        
        # traverse all courses
        for course in range(numCourses):
            if not dfs(course):
                # cycle found
                return False

        return True

