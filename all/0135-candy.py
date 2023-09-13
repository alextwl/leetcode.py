'''
2023/09/13 daily challenge

two-pass greedy approach

scan from both head and tail of array,
increase the distribution of candies only when the next child's rating is greater,
or leave it unchanged.

(hint: children may get only 1 candy even if its rating was equal to neighbors
       who had many more candies.)
'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)  # each child has at least 1 candy.
        
        # scan from left
        it = enumerate(ratings)
        i, prev_rate = next(it)
        
        for j, rate in it:
            if rate > prev_rate:
                # child with a higher rating get one more candies than the left neighbor.
                candies[j] = candies[i] + 1
            # if not, we can give the current child only 1 candy to minimize the cost. :)
            
            i, prev_rate = j, rate
        
        # scan from right
        it = enumerate(reversed(ratings), start=1)
        i, prev_rate = next(it)
        
        for j, rate in it:
            '''
            child with a higher rating get one more **or** many more candies than the right neighbor.
            '''
            if rate > prev_rate:
                candies[-j] = max(candies[-i] + 1, candies[-j])
            
            i, prev_rate = j, rate

        return sum(candies)

