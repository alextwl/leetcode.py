'''
2025/03/03 daily challenge

dynamic arrays approach
'''


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        pivot_count = 0
        right = []

        for v in nums:
            if v < pivot:
                left.append(v)
            elif v > pivot:
                right.append(v)
            else:
                pivot_count += 1
        return left + [pivot] * pivot_count + right


'''
fixed array approach
'''


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        ans = [pivot] * n

        for i, j in zip(range(n), range(n-1, -1, -1)):
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
            if pivot < nums[j]:
                ans[right] = nums[j]
                right -= 1

        return ans

