'''
2026/10/17 daily challenge

counting cycles approach
'''


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        dig_vals = [(sum(map(int, s)), orig, i) for i, (s, orig) in enumerate(zip(map(str, nums), nums))]
        dig_vals.sort()

        i_to_dvi = [0] * n
        for dvi, (_, _, i) in enumerate(dig_vals):
            i_to_dvi[i] = dvi

        # count cycles
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = i_to_dvi[j]

        return n - cycles

