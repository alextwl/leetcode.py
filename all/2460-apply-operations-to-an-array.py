'''
2025/03/01 daily challenge

count zero elements approach
'''


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zero_count = 0
        ans = []  # positive integers only

        it = iter(nums)
        a = next(it)
        for b in it:
            if a == b:
                a = a * 2
                b = 0
            if a:
                ans.append(a)
            else:
                zero_count += 1
            a = b
        # proceed last element
        if a:
            ans.append(a)
        else:
            zero_count += 1

        return ans + [0] * zero_count

