'''
leetcode 75 lv2 day 5

count the max idle slots and determine if it's enough to fill all other tasks.
'''

import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        counts = collections.Counter(tasks)
        maxcount = max(counts.values())

        '''
        schedule the task with maximum frequency, and allocate its idle times.
        the last task does not need to idle when finishing, let's count it later.

        e.g. A * 3, n = 2
             A -> idle -> idle -> A -> idle -> idle. [-> last A task, to be added later.]
        
        and then we can fill the idle slots with all other tasks with fewer frequencies.
        '''

        runtime = (maxcount-1) * (n+1)  # (max freq - last task) * (idles + task itself)

        '''
        if there's any task has max frequency, its last task extends the overall runtime.
        '''
        for freq in counts.values():
            if freq == maxcount:
                runtime += 1

        '''
        the idle slots of max freq task may not be enough to fill all other tasks.
        in this case, the least time is equal to the size of the tasks.
        '''
        return max(runtime, len(tasks))

