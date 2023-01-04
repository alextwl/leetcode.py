'''
2023/01/03 daily challenge

counter approach
'''

import collections

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        levels = collections.Counter(tasks)
        minRounds4Amount = dict()
        rounds = 0

        for amount in levels.values():
            if amount == 1:
                # we cannot complete it because there's only 1 task of current level.
                return -1
            
            # see if the number of task amount was calculated before
            if minRounds := minRounds4Amount.get(amount):
                rounds += minRounds
                continue

            # time to calculate the minimum rounds required for current level
            q, r = divmod(amount, 3)
            if r == 0:
                '''
                we can complete q rounds of 3 tasks of current level with no unfinished task.
                the minimum rounds required for current level is q.
                '''
                rounds += q
                minRounds4Amount[amount] = q  # memorize the answer for the current amount
            else:
                '''
                for r == 1:
                we can complete q rounds of 3 tasks of current level with leaving 1 unfinished task.
                let's rearrange it to (q-1) rounds of 3 tasks + 2 rounds of 2 tasks,
                so that the minimum rounds required for current level is (q-1) + 2 = q+1.

                for r == 2:
                we can complete q rounds of 3 tasks + 1 round of 2 tasks of current level.
                the minimum rounds required for current level is q+1.
                '''
                rounds += q + 1
                minRounds4Amount[amount] = q + 1  # memorize the answer for the current amount

        return rounds

