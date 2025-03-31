'''
2023/07/08 daily challenge
2025/03/31 daily challenge

sorting approach

learnt from official solution
https://leetcode.com/problems/put-marbles-in-bags/solution/

sort all the adjacent elements as a pair on the spliting point,
and get max & min scores.
'''

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pair_weights = [0] * (n-1)

        w_it = iter(weights)
        prev = next(w_it)
        for i in range(0, n-1):
            current = next(w_it)
            pair_weights[i] = prev + current
            prev = current

        # sort these pairs (the candidates of k-1 splitting point)
        pair_weights.sort()

        '''
        no need to include weights[0] & weights[n-1] because
        both minScore & maxScore have them, and their difference will cancel it.
        '''
        ans = 0

        min_it = iter(pair_weights)
        max_it = reversed(pair_weights)
        # pick k-1 max & min pairs and get its difference.
        for _ in range(k-1):
            ans += next(max_it) - next(min_it)

        return ans


'''
sorting + sum diff approach

the score of distribution is the sum of bag scores which consist of
weights of left & right bounds, it's equivalent to

"1st marble + marbles in the both sides of split points + last marble",

so that we can change the problem to

max(k-1 split point scores) - min(k-1 split point scores).

no need to count 1st & last marbles because the diff cancels it eventually.
'''


import itertools


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            # shortcut for speedup
            return 0
        n = len(weights)
        split_points = [a + b for a, b in itertools.pairwise(weights)]
        split_points.sort()
        return sum(split_points[-k+1:]) - sum(split_points[:k-1])

