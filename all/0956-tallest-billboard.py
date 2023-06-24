'''
2023/06/24 daily challenge

exhaustive approach

learnt from official solution (meet in the middle):
https://leetcode.com/problems/tallest-billboard/solution/
'''

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def get_common_height_by_diff(rods):
            '''
            build every combination of two steels by given rods,
            and return maximum height of two steels by difference.
            
            e.g. for (4,3) pair, dp[4-3] = dp[1] = 4.
            for (5,7) pair, dp[5-7] = dp[-2] = 5
            '''
            steel_pairs = {(0, 0)}
            for r in rods:
                new_pairs = set()
                for left, right in steel_pairs:
                    '''
                    concatenate current rod to both left and right steels of each pair.
                    '''
                    new_pairs.add((left + r, right))
                    new_pairs.add((left, right + r))
                # union
                steel_pairs |= new_pairs
            # calculate the maximum heights by difference of each pair.
            dp = dict()
            for left, right in steel_pairs:
                diff = left - right
                dp[diff] = max(dp.get(diff, 0), left)

            return dp
        
        middle = len(rods) // 2
        dp1 = get_common_height_by_diff(rods[:middle])
        dp2 = get_common_height_by_diff(rods[middle:])
        
        ans = 0
        for diff in dp1:
            if -diff in dp2:
                ans = max(ans, dp1[diff] + dp2[-diff])

        return ans


'''
dynamic programming approach

learnt from official solution:
https://leetcode.com/problems/tallest-billboard/solution/

we memorize only (taller, smaller) pairs to reduce the complexity.
'''

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        '''
        each pair of steels has a taller and a shorter steel.
        dp[taller - shorter] = the maximum height of a taller
        dp[0] = the maximum height of two steels with equal length (diff=0.)
        '''
        dp = {0: 0}
        
        for r in rods:
            # add a rod to current steels.
            new_dp = dp.copy()
            
            for diff, taller in dp.items():
                shorter = taller - diff
                
                # add new rod to the taller one with a positive diff.
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
                
                '''
                add new rod to the smaller one,
                and generate a new non-negative diff.
                '''
                new_diff = abs(shorter+r - taller)
                # if (shorter+r) is longer than the taller, replace the old taller.
                new_taller = max(shorter+r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0),
                                       new_taller)
            dp = new_dp
        
        # if dp[0] didn't exist, the billboard cannot be supported.
        return dp.get(0, 0)

