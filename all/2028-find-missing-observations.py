'''
2024/09/05 daily challenge
'''


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        point_needed = mean * (m + n) - sum(rolls)

        if point_needed < n:
            # each roll should be at least 1
            return []
        
        quo, rem = divmod(point_needed, n)
        
        if quo > 6 or (quo == 6 and rem):
            # impossible to find rolls > 6
            return []

        ans = []
        for _ in range(rem):
            ans.append(quo + 1)
        for _ in range(n - rem):
            ans.append(quo)

        return ans

