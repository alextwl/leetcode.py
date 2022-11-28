'''
programming skills lv1 day 1

time=O(n), one-pass is faster than oneliner which may run multipass.
'''

class Solution:
    def average(self, salary: List[int]) -> float:
        # (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
        total, minimum, maximum = 0, float('inf'), float('-inf')

        for money in salary:
            total += money
            minimum = min(minimum, money)
            maximum = max(maximum, money)
        
        return (total - minimum - maximum) / (len(salary) - 2)

