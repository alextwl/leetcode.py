'''
2025/11/09 daily challenge

simulation with division speed up
'''


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1 and num2:
            if num1 >= num2:
                op, num1 = divmod(num1, num2)
            else:
                op, num2 = divmod(num2, num1)
            ans += op
        return ans


'''
euclidean algorithm approach
'''


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        # if num1 < num2, no operation is done,
        # there's only a swap between num1 & num2.
        while num1 and num2:
            op, num1 = divmod(num1, num2)
            ans += op
            num1, num2 = num2, num1
        return ans

