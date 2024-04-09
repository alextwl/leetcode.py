'''
2024/04/09 daily challenge

one-pass calculation approach

intuition: the time needed =

sum(min(t[0],t[k]), min(t[1],t[k]), ..., t[k], min(t[k+1], t[k]-1), min(t[k+2], t[k]-1), ...)
'''


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = threshold = tickets[k]
        
        for i in range(k):
            ans += min(tickets[i], threshold)
        
        # for max time needed to buy tickets after k-th people
        threshold -= 1

        # shortcut: all ticket bought, no need to iterate after k-th people
        if not threshold:
            return ans

        for i in range(k+1, len(tickets)):
            ans += min(tickets[i], threshold)

        return ans

