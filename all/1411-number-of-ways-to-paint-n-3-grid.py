'''
2026/01/03 daily challenge

dynamic programming approach

prepare for the relationship between adjacent rows,
and the calculate the number of ways with DP.
'''


# R=0 Y=1 G=2
# G[CCC] = list of possible combinations of prev/next rows.
G = {"010": ["101", "102", "121", "201", "202"],
     "012": ["101", "120", "121", "201"],
     "020": ["101", "102", "201", "202", "212"],
     "021": ["102", "202", "210", "212"],
     "101": ["010", "012", "020", "210", "212"],
     "102": ["010", "020", "021", "210"],
     "120": ["012", "201", "202", "212"],
     "121": ["010", "012", "202", "210", "212"],
     "201": ["010", "012", "020", "120"],
     "202": ["010", "020", "021", "120", "121"],
     "210": ["021", "101", "102", "121"],
     "212": ["020", "021", "101", "120", "121"]}


class Solution:
    def numOfWays(self, n: int) -> int:
        # base case: first row's combinations
        dp0 = {ccc: 1 for ccc in G.keys()}
        dp1 = dict()

        for _ in range(n - 1):
            for curr in G.keys():
                # calculate the number of possible combinations
                # ending at curr row.
                # e.g.
                # dp["012"] = prev number of ways
                #             ending at ["101", "120", "121", "201"]
                dp1[curr] = sum(dp0[ccc] for ccc in G[curr]) % 1_000_000_007
            dp0, dp1 = dp1, dp0

        # summarize numbers of ways ending at all kinds of rows.
        return sum(dp0.values()) % 1_000_000_007

