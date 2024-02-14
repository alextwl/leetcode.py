'''
2024/02/14 daily challenge

divide & merge approach
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        left, right = [], []

        for v in nums:
            if v < 0:
                left.append(v)
            else:
                right.append(v)

        ans = []
        for a, b in zip(left, right):
            # rearranged array begins with a positive integer
            ans.append(b)
            ans.append(a)

        return ans

