'''
2024/12/18 daily challenge

brute force approach
'''


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []  # reversed

        for i in range(n - 1, -1, -1):
            p = prices[i]
            j = i + 1
            while j < n:
                if prices[j] <= p:
                    ans.append(p - prices[j])
                    break
                else:
                    j += 1
            else:
                ans.append(p)

        ans.reverse()
        return ans


'''
monotonic stack approach

the current price (prices[j]) when iterating
is always the nearest to top of stack (prices[i]),
and after prices[i] discounted it's popped.
'''


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # indices of previous purchases to be discounted
        ans = prices.copy()

        for i, p in enumerate(prices):
            # apply discounts to all previous purchases
            while stack and prices[stack[-1]] >= p:
                ans[stack.pop()] -= p

            # queue the current purchase for further discount
            stack.append(i)

        return ans

