'''
min/max heaps approach
'''


import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # backlogs: min heap for sell side, max heap for buy side
        # [(price, amount), ...]
        h_buy = []
        h_sell = []

        for p, a, t in orders:
            if t == 0:
                # buy side, match cheapest sell orders
                # until buy orders fulfilled or sell backlog exhausted
                while a > 0 and h_sell and h_sell[0][0] <= p:
                    a, h_sell[0][1] = a - h_sell[0][1], h_sell[0][1] - a
                    if h_sell[0][1] <= 0:
                        heapq.heappop(h_sell)
                if a > 0:
                    heapq.heappush(h_buy, [-p, a])
            else:
                # sell side, match the most expensive buy orders
                # until sell orders fulfilled or buy backlog exhausted
                while a > 0 and h_buy and -h_buy[0][0] >= p:
                    a, h_buy[0][1] = a - h_buy[0][1], h_buy[0][1] - a
                    if h_buy[0][1] <= 0:
                        heapq.heappop(h_buy)
                if a > 0:
                    heapq.heappush(h_sell, [p, a])
        return (sum(v[1] for v in h_buy) + sum(v[1] for v in h_sell)) % 1_000_000_007

