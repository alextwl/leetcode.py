'''
2025/03/16 daily challenge

binary search approach
'''


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def validate(minutes):
            repaired = 0
            for r in ranks:
                repaired += int((minutes / r) ** 0.5)
                if repaired >= cars:
                    return True
            return False
        
        l, r = 0, max(ranks) * 1_000_000_000_000
        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

