'''
2024/06/19 daily challenge

binary search approach

search the minimum required day and
calculate the number of bouquets every loop of searching.
'''


class Solution:
    def minDays(self, bloomdays: List[int], m: int, k: int) -> int:
        def get_bouquets(target):
            blossom = 0
            adj_count = 0
            
            for d in bloomdays:
                if d <= target:
                    adj_count += 1
                else:
                    adj_count = 0
                
                # check if required number of adjacent flowers bloomed
                if adj_count == k:
                    blossom += 1
                    adj_count = 0
            
            return blossom
        
        # shortcut: insufficient flowers
        if len(bloomdays) < m * k:
            return -1

        # binary search the minimum bloom day.
        left, right = 0, max(bloomdays)
        ans = -1

        while (left <= right):
            mid = (right - left) // 2 + left

            if (b := get_bouquets(mid)) >= m:
                # although get_bouquets(mid) == m,
                # mid might not be minimized, so we need to continue
                # searching until left > right in order to ensure
                # the latest mid is minimized.
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

