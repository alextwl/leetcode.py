'''
maximize the grestest and replace elements reversely.
'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        ans = []
        for v in reversed(arr):
            ans.append(greatest)
            greatest = max(greatest, v)
        ans.reverse()
        return ans

