'''
always fill cups with top-2 remaining amount of water every second
'''


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        sec = 0

        while amount[2]:
            sec += 1
            if amount[1]:
                amount[1] -= 1
            amount[2] -= 1
            amount.sort()

        return sec

