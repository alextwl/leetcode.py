'''
2023/03/31 daily challenge

dynamic programming by cache

just cut the pizza in every ways and count the number of ways
of cutting the pizza satisfied the requirement.
'''


import functools


MODULO = 10 ** 9 + 7


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        @functools.cache
        def contains_apple(top, left, bottom, right):
            '''
            check if the area of pizza[top][left] ~ pizza[bottom][right]
            contains apple.
            '''
            for i in range(top, bottom+1):
                for j in range(left, right+1):
                    if pizza[i][j] == 'A':
                        # at least one apple found
                        return True
            # apple not found
            return False

        @functools.cache
        def cut_pizza(top, left, slices_needed):
            '''
            cut pizza[top][left] ~ pizza[-1][-1] into slices_needed pieces.
            '''
            if slices_needed == 1:
                # no need to cut more, check the current slice.
                if contains_apple(top, left, m-1, n-1):
                    return 1
                else:
                    return 0

            valid_ways = 0
            # cut horizontally
            for i in range(top+1, m):
                '''
                cut into 2 slices, if the upper slice has apple,
                then we can try to cut the lower slice into more slices.

                in other words, if the upper slice has no apple,
                then this cut is not valid because the slice does not meet the requirement
                and cannot be counted.

                upper: pizza[top][left] ~ pizza[i-1][n-1]
                lower: pizza[i][left] ~ pizza[m-1][n-1]
                '''
                if contains_apple(top, left, i-1, n-1):
                    valid_ways += cut_pizza(i, left, slices_needed-1)
            # cut vertically
            for j in range(left+1, n):
                '''
                cut into 2 slices, if the left slice has apple,
                then we can try to cut the right slice into more slices.

                left: pizza[top][left] ~ pizza[m-1][j-1]
                right: pizza[top][j] ~ pizza[m-1][n-1]
                '''
                if contains_apple(top, left, m-1, j-1):
                    valid_ways += cut_pizza(top, j, slices_needed-1)

            return valid_ways

        return cut_pizza(0, 0, k) % MODULO

