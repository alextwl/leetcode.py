'''
2023/12/06 daily challenge

simulation approach

calculate each week's money and sum up.
'''


class Solution:
    def totalMoney(self, n: int) -> int:
        quo, rem = divmod(n, 7)
        
        total = 0
        # add money of each complete week.
        for week in range(quo):
            sunday = week + 7
            total += ((sunday * (sunday+1)) >> 1) - ((week * (week+1)) >> 1)

        # add money of the last incomplete week.
        for money in range(quo+1, quo+rem+1):
            total += money

        return total

