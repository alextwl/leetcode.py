'''
2024/06/21 daily challenge

sliding window approach
'''


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # accumulate all satisfied customers first
        ans = sum(c for c, g in zip(customers, grumpy) if not g)
        
        # sliding window: use power to override unsatisfied customers
        # accumulate customers in the grumpy minutes within the initial window
        for i in range(minutes):
            if grumpy[i]:
                ans += customers[i]
        
        current_satisfied = ans
        left = 0
        for right in range(minutes, len(customers)):
            # proceed only grumpy minutes
            if grumpy[left]:
                current_satisfied -= customers[left]
            left += 1
            if grumpy[right]:
                current_satisfied += customers[right]
                ans = max(ans, current_satisfied)

        return ans

