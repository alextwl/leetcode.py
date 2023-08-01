'''
2023/08/01 daily challenge

iterative breakdown approach
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = [[]]
        for _ in range(k):
            new_combs = []
            for comb in ans:
                '''
                select 1..comb[0] or 1..n,
                if comb[0] == 1 then the current combination is discarded
                because of insufficient numbers chosen.
                '''
                j = comb[0] if comb else n+1
                for i in range(1, j):
                    new_combs.append([i] + comb)
            ans = new_combs

        return ans

