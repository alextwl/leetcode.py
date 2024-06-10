'''
2024/06/10 daily challenge

oneliner using built-in sorting function
'''


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))


'''
bubble sort approach
'''


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(n - i - 1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            return arr
        return sum(a != b for a, b in zip(heights, bubble_sort(heights.copy())))

