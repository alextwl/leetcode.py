'''
2023/07/08 daily challenge

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

