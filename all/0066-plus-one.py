'''
2026/01/01 daily challenge
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        
        for idx in range(len(digits)-1, -1, -1):
            digits[idx] += carry
            if digits[idx] >= 10:
                carry = 1
                digits[idx] -= 10
            else:
                carry = 0
        if carry:
            digits = [1] + digits
        return digits


'''
stack approach
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stack = []
        while digits:
            digits[-1] += 1
            if digits[-1] < 10:
                break
            digits.pop()
            stack.append(0)
        else:
            stack.append(1)
        while stack:
            digits.append(stack.pop())
        return digits

