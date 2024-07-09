'''
2024/07/09 daily challenge

simulation approach
'''


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitings = 0  # the total waiting time
        last_order = 0  # the time chef finishes the last order

        for arrival, cost in customers:
            if last_order <= arrival:
                # chef is idle now, reset the timer.
                last_order = arrival + cost
            else:
                # chef is busy, queue it.
                last_order += cost

            waitings += last_order - arrival

        return waitings / len(customers)

