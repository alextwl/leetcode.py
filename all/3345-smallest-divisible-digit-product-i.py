'''
2026/08/06 daily challenge

table lookup method approach
'''


PRODUCT = list(range(10))  # 0..9


# 10..99
for i in range(1, 10):
    for j in range(0, 10):
        PRODUCT.append(i * j)


PRODUCT.append(0)  # 100


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for m in range(n, 101):
            if PRODUCT[m] % t == 0:
                return m

