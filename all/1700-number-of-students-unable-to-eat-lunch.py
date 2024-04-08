'''
2024/04/08 daily challenge

simulation approach
'''

import collections


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # note the problem defines i=0 is the top of the stack,
        # reverse it in order to utilitize pop function
        sandwiches.reverse()
        q = collections.deque(students)

        # the total number of square sandwitches students needed
        squares = sum(students)
        # the total number of circular sandwitches students needed
        circulars = len(students) - squares

        while(q and sandwiches):
            req = q.popleft()

            if req == sandwiches[-1]:
                sandwiches.pop()
                if req == 0:
                    circulars -= 1
                else:
                    squares -= 1
            else:
                q.append(req)

            # early break for infinite loops if no more student would take
            # the top sandwich
            if sandwiches and (
                    (sandwiches[-1] == 0 and circulars == 0) or
                    (sandwiches[-1] == 1 and squares == 0)):
                break

        return len(q)


'''
counter approach
'''


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # the remaining number of square sandwitches students needed
        squares = sum(students)
        # the remaining number of circular sandwitches students needed
        circulars = len(students) - squares

        # iterate sandwiches and for each loop
        # consider if we could serve the remaining students the top sandwich.
        for sw in sandwiches:
            # early break for infinite loops if no more student would take
            # the top sandwich
            if (sw == 0 and circulars == 0) or (sw == 1 and squares == 0):
                break
            
            # sandwich served
            if sw == 0:
                circulars -= 1
            else:
                squares -= 1

        return squares + circulars

