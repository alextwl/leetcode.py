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


'''
python built-in oneliner ver
'''

import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
         n
        C
         k
        '''
        return list(itertools.combinations(range(1, n+1), k))


'''
top-down recursive ver
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]

        '''
        Pascal's rule:

         n    n-1    n-1
        C  = C    + C
         k    k      k-1

        See https://en.wikipedia.org/wiki/Pascal%27s_rule
        '''
        ans = []
        for i in range(k, n+1):
            for prefix in self.combine(i-1, k-1):
                ans.append(prefix + [i])

        return ans

