'''
2022/10/16 daily challenge

dynamic programming + DFS recursive approach

learnt from
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/discuss/490316/JavaC%2B%2BPython3-DP-O(nd)-Solution

the idea is iterating all possible subarrays for both days & jobs.
'''


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        if n < d:
            # insufficient jobs to be scheduled on each day.
            return -1
        
        dp = [dict() for _ in range(n)]
        
        def dfs(i, day):
            if day == 1:
                '''
                when there's only 1 day where jobs can be scheduled for,
                the minimum difficulty of the schedule is the maximum difficulty of the remaining jobs.
                the ultimate round of loop stops here.
                '''
                return max(jobDifficulty[i:])
            
            if day in dp[i]:
                return dp[i][day]
            
            min_cost = float('inf')  # minimum difficulty for jobDifficulty[i:] in specific range of days.
            job_max = 0  # the maximum difficulty of a job of a single day.
            
            '''
            job_max may increase when multiple jobs are adding to a day continuously during the loop.
            '''
            for j in range(i, n - day + 1):
                job_max = max(job_max, jobDifficulty[j])  # add one more job to a day.
                min_cost = min(min_cost, job_max + dfs(j+1, day-1))  # minimum difficulty of the schedule with a smaller problem
                                                                     # (remaining jobs & tomorrow:d)
            
            dp[i][day] = min_cost
            
            return min_cost
        
        return dfs(0, d)

