'''
leetcode 75 lv2 day 11

depth first search approach
'''

import collections


NOT_YET_CHECKED = 0  # the course is not yet traversed
CHECKING_CHILDREN = 1  # checking the childern of the course. (the status is for detecting cyclic.)
COURSE_QUEUED = 2  # the course is traversed and added to the stack.


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        status = [NOT_YET_CHECKED] * numCourses  # the status of input courses.

        course_stack = []  # the reversed order of courses to be enrolled.
        cycle_found = False  # if a cycle is found, it's impossible to finisl all courses.

        '''
        build tree

        prerequisites[i] = [ai, bi]
        bi -> ai: directed connected
        '''
        prereq2courses = collections.defaultdict(set)
        for course, prereq in prerequisites:
            prereq2courses[prereq].add(course)

        def dfs(course):
            nonlocal cycle_found
            if cycle_found:
                # a cycle is found, no need to search further.
                return
            
            # mark the course to start checking
            status[course] = CHECKING_CHILDREN

            for child in prereq2courses[course]:
                if status[child] == NOT_YET_CHECKED:
                    dfs(child)
                elif status[child] == CHECKING_CHILDREN:
                    '''
                    we traversed a child which is also checking its childern,
                    it's cyclic that we cannot finidh these courses depending on the prerequisites.
                    '''
                    cycle_found = True
                    return
                '''
                if child was already COURSE_QUEUED, no need to traverse it again
                because it's already after the input course as its prequisite.
                '''

            course_stack.append(course)
            status[course] = COURSE_QUEUED
            return

        # traverse all courses
        for course in range(numCourses):
            if cycle_found:
                return []
            if status[course] == NOT_YET_CHECKED:
                dfs(course)

        return [] if cycle_found else course_stack[::-1]

