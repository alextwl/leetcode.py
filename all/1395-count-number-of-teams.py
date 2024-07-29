'''
2024/07/29 daily challenge

dynamic programming approach (tabulation)
'''


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        
        inc_teams = [{i: 0 for i in range(1,4)} for _ in range(n)]
        dec_teams = [{i: 0 for i in range(1,4)} for _ in range(n)]
        
        # base case: each soldier forms a team of single member
        for i in range(n):
            inc_teams[i][1] = 1
            dec_teams[i][1] = 1
        
        for cnt in [2, 3]:
            # count all increasing/decreasing teams of 2 & 3 members
            for i in range(n):
                for j in range(i + 1, n):
                    if rating[j] > rating[i]:
                        inc_teams[j][cnt] += inc_teams[i][cnt-1]
                    if rating[j] < rating[i]:
                        dec_teams[j][cnt] += dec_teams[i][cnt-1]
        
        for a, b in zip(inc_teams, dec_teams):
            ans += a[3] + b[3]

        return ans

