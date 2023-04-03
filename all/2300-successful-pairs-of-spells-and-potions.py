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


'''
binary search + two pointer approach
'''


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = [None] * len(spells)  # succeeded products
        m = len(potions)
        potions.sort()

        # sort the spells in descending order and remember its original indexes
        desc_spells = sorted(enumerate(spells), key=lambda v:v[1], reverse=True)

        # optimize the search by two pointer approach.
        # since we've sorted the spells,
        # no need to reset left pointer to zero
        # so that we can save the time of binary search.
        left = 0
        for i, s in desc_spells:
            right = m - 1
            while(left <= right):
                mid = left + ((right-left)>>1)
                product = s * potions[mid]
                if product < success:
                    left = mid + 1
                else:
                    right = mid - 1
            # count succeeded products
            ans[i] = m - left

        return ans

