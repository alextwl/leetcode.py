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

