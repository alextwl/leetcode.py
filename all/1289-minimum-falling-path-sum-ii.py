'''
2024/04/26 daily challenge

dynamic programming approach
'''


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def find_min2(row_list):
            '''
            find the first 2 smallest numbers.
            '''
            first_idx = second_idx = None
            first_val = second_val = float('inf')

            for i, val in enumerate(row_list):
                if val < first_val:
                    second_idx, second_val = first_idx, first_val
                    first_idx, first_val = i, val
                elif val < second_val:
                    second_ifx, second_val = i, val

            return (first_idx, first_val, second_idx, second_val)

        n = len(grid)
        it = iter(grid)
        # assign the first row as the previous row (dp space)
        prev = next(it)

        for row in it:
            min1_idx, min1_val, min2_idx, min2_val = find_min2(prev)
            for j in range(n):
                if j == min1_idx:
                    # the 1st minimum cell of previous row is adjacent to the current cell,
                    # use the 2nd one.
                    row[j] += min2_val
                else:
                    row[j] += min1_val
            prev = row

        return min(prev)

