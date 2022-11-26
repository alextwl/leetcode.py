'''
2022/11/26 daily challenge

dynamic programming approach

learnt from
https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
https://leetcode.com/discuss/comment/368880
https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/733167/Thinking-process-Top-down-DP-Bottom-up-DP
'''

import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
        reduce the problem by sorting the endTime of jobs in ascending order,
        and then we can consider startTime later.
        '''
        jobs = sorted(zip(startTime, endTime, profit), key=lambda t: t[1])
        
        '''
        dp[i] = [the endTime of last scheduled job, max earned profit at this point]
        
        jobs are sorted in ascending endTime, we are going to determine
        whether to schedule jobs with possible time range,
        so we default dp to a dummy job which is scheduled and ended at the beginning with zero profit.
        '''
        dp = [[0, 0]]
        
        for jStart, jEnd, jProfit in jobs:
            '''
            find the index of nearest *previous* job where the current job can be scheduled ending with.
            
            the reason to binary search it by [jStart+1] then -1 is because
            we want to find the nearest previous job where:
            (1) the current job may be scheduled just after such previous job continuously.
            (2) select the last scheduled one if there're multiple previous jobs with the same endTime <= current startTime
                (e.g. dp = [[3, 0], [3, 1], [4, 2]] and we want to find the previous one with endTime=3,
                      it bisects dp with startTime=4, returns index=2 which point to [4, **],
                      and we shift to a previous job, which is index=1.)
            '''
            i = bisect.bisect_left(dp, [jStart+1]) - 1
            if (totalProfit := dp[i][1] + jProfit) > dp[-1][1]:
                '''
                if the nearest previous job's total profit + current job's profit
                was greater than the last scheduled max profit,
                the current job can be scheduled after the i-th dp job.
                '''
                dp.append([jEnd, totalProfit])
        
        # the last scheduled job has the maximum total profit.
        return dp[-1][1]

