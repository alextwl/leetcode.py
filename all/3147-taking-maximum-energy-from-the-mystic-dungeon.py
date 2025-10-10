'''
2025/10/10 daily challenge

accumulations separated by modulo k
'''


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        arr = [float('-inf')] * k
        for i, v in enumerate(energy):
            j = i % k
            if arr[j] < 0:
                arr[j] = v
            else:
                arr[j] += v
        return max(arr)

