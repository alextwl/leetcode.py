'''
2023/04/02 daily challenge

binary search approach

just search the target product.
'''

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []  # succeeded products
        m = len(potions)
        potions.sort()

        for s in spells:
            left, right = 0, m - 1
            while(left <= right):
                mid = left + ((right-left)>>1)
                product = s * potions[mid]
                if product < success:
                    left = mid + 1
                else:
                    right = mid - 1
            # count succeeded products
            ans.append(m - left)

        return ans

