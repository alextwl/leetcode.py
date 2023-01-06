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

