'''
2023/03/01 daily challenge

heap sort approach
'''


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n, i):
            left = (i<<1) + 1
            right = (i<<1) + 2
            largest = i

            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if largest != i:
                # swap i & largest
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        for i in range(len(nums)>>1, -1, -1):
            heapify(len(nums), i)

        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(i, 0)

        return nums

