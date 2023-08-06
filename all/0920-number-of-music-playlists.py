'''
2023/08/06 daily challenge

dynamic programming approach
'''


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        '''
        dp space:
        dp[n][goal] = the number of possible playlists for (n, goal) with k repeat limit.
        
        base case: there's an empty playlist, which is also a playlist, for n=0, goal=0.
        '''
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        
        for i in range(1, goal+1):
            '''
            minimize the range of n different songs because
            we want every song to be played at least once within limited plays (when i<n).
            '''
            for j in range(1, min(i, n)+1):
                '''
                the i-th song can be a new song we haven't played before,
                which were (n - j + 1) songs. (== the number of possible songs of the j-th song.)
                '''
                dp[i][j] = dp[i-1][j-1] * (n-j+1)
                
                '''
                plus if we can replay any songs we've played before
                when we've played k other songs.
                the songs we can replay are the 1st to the (j-k)-th song **for the same goal.**
                
                (we cannot select an old song from a previous goal == the shorter playlist `j-1`
                because we need to calculate the difference between j & k
                and if we shorten the playlist, it couldn't include all j songs we've played before.)
                '''
                if j > k:
                    dp[i][j] += dp[i-1][j] * (j - k)

        return dp[-1][-1] % 1_000_000_007

