'''
2023/12/04 daily challenge

iterative approach
'''


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ''
        prev2 = prev1 = None
        for c in num:
            if prev2 == prev1 == c:
                if c > largest:
                    largest = c
                    if c == '9':
                        return '999'
            prev2, prev1 = prev1, c

        return largest * 3 if largest else ''

