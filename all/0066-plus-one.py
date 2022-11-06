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
