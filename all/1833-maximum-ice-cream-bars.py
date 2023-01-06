'''
2023/01/06 daily challenge

sorting + greddy approach
'''

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        costs.sort()
        for price in costs:
            if price > coins:
                break
            coins -= price
            ans += 1
        return ans


'''
counting sort approach
'''

import collections

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        counts = collections.Counter(costs)

        for i in range(1, max(counts.keys())+1):
            if i not in counts:
                continue
            quo = min(coins//i, counts[i])
            if not quo:
                # coins exhausted
                break
            ans += quo
            coins -= quo*i

        return ans

