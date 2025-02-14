'''
2025/02/14 daily challenge

prefix sum (product) approach
'''


class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]       # prefix product
        self.prefix_zero = [0]  # prefix occurance of zero
        self.overall = 1        # overall product
        self.overall_zero = 0   # overall occurance of zero

    def add(self, num: int) -> None:
        if num:
            # non-zero product
            self.overall *= num
        else:
            # count the zero
            self.overall_zero += 1

        self.prefix.append(self.overall)
        self.prefix_zero.append(self.overall_zero)

    def getProduct(self, k: int) -> int:
        j = len(self.prefix) - k - 1
        if self.overall_zero - self.prefix_zero[j]:
            # there are one or more occurances of zeroes in the last k integers.
            return 0
        return self.overall // self.prefix[j]

