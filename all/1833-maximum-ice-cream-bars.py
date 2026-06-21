'''
2023/01/06 daily challenge
2026/06/21 daily challenge

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
counter approach
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


'''
counting sort approach
'''


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0] * (max(costs) + 1)
        for price in costs:
            counts[price] += 1

        bought = 0
        for price, bars in enumerate(counts):
            if price > coins:
                break
            if not bars:
                continue

            can_buy = min(bars, coins // price)
            bought += can_buy
            coins -= can_buy * price

        return bought

