'''
2024/08/15 daily challenge

simulation approach
'''


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_5 = bill_10 = bill_20 = 0
        for v in bills:
            # provide changes
            changes = v - 5
            while bill_20 and changes >= 20:
                bill_20 -= 1
                changes -= 20
            while bill_10 and changes >= 10:
                bill_10 -= 1
                changes -= 10
            while bill_5 and changes >= 5:
                bill_5 -= 1
                changes -= 5
            if changes:
                # cannot provide customer with enough change
                return False
            # pay the bill
            if v == 5:
                bill_5 += 1
            elif v == 10:
                bill_10 += 1
            else:
                bill_20 += 1
        return True

