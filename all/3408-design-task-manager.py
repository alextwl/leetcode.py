'''
2025/09/18 daily challenge

max heap + sorted list approach
'''


import bisect
import heapq


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_uid = dict()
        self.task_priority = dict()
        self.priority_tasks = dict()
        self.priorities = []  # max heap of priority number

        for t in tasks:
            self.add(*t)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_uid[taskId] = userId
        self.task_priority[taskId] = priority
        if priority not in self.priority_tasks:
            self.priority_tasks[priority] = [taskId]
            heapq.heappush(self.priorities, -priority)
        else:
            l = self.priority_tasks[priority]
            i = bisect.bisect_right(l, taskId)
            l.insert(i, taskId)

    def edit(self, taskId: int, newPriority: int) -> None:
        self.priority_tasks[self.task_priority[taskId]].remove(taskId)
        self.add(self.task_uid[taskId], taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        self.priority_tasks[self.task_priority[taskId]].remove(taskId)

    def execTop(self) -> int:
        while self.priorities:
            p = -self.priorities[0]
            if self.priority_tasks[p]:
                return self.task_uid[self.priority_tasks[p].pop()]
            else:
                del self.priority_tasks[p]
                heapq.heappop(self.priorities)
        return -1

