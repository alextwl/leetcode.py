'''
2022/12/29 daily challenge

heap approach

(1) index the tasks, and sort it by enqueueTime in descending order.
(2) use minheap to enqueue tasks which are able to be scheduled.
(3) run task from minheap sorted by processingTime.
'''

from heapq import heappop, heappush


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        avail_tasks = [(enqTime_procTime[0], enqTime_procTime[1], index) for index, enqTime_procTime in enumerate(tasks)]
        '''
        sort avail_tasks by the first element of a tuple (enqueueTime)
        and reverse the order for the convenience of further popping.
        '''
        avail_tasks.sort()
        avail_tasks.reverse()

        currentTime = 0
        h = []  # a heap of queued tasks to be scheduled. (value: (processingTime, index))
        task_seq = []  # the sequence of scheduled task indexes (answer)

        while(avail_tasks or h):
            if (not h and avail_tasks and avail_tasks[-1][0] > currentTime):
                # skip idle time to the earlist euqueue task
                currentTime = avail_tasks[-1][0]
                #print("update currentTime=%d" % currentTime)

            # enqueue tasks based on currentTime
            while(avail_tasks and avail_tasks[-1][0] <= currentTime):
                enqueueTime, processingTime, index = avail_tasks.pop()
                heappush(h, (processingTime, index))
                #print("enqueue task=(%d,%d,%d)" % (enqueueTime, processingTime, index))

            # run task from minheap
            processingTime, index = heappop(h)
            currentTime += processingTime
            task_seq.append(index)
            #print("task %d proceeded, currentTime=%d" % (index, currentTime))
        
        return task_seq

