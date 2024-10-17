'''
2024/10/17 daily challenge

sorting + two-pass iteration approach

(1) find the max digit (rightmost one if there're multiple) misaligned to the sorted one
(2) find the digit smaller than the max digit and its index is smallest (leftmost)
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(enumerate(map(int, list(str(num)))))
        digits.sort(key=lambda x: (-x[1], -x[0]))  # note: let the same value with

        # 1st pass: find the max digit whose index is not aligned to sorted digits 
        max_digit_i = -1
        max_digit = -1
        for j, (i, v) in enumerate(digits):
            if j == i:
                # if its index is the same to the sorted one, skip
                continue
            if digits[i][1] == v:
                # if its value equals to the sorted one's value, also skip
                continue
            max_digit, max_digit_i = v, i
            break
        else:
            # no need to swap
            return num

        # 2nd pass: find a smaller digit but its index is much further to the left
        target_i = 10
        for i, v in digits:
            if v >= max_digit:
                continue
            target_i = min(target_i, i)

        # do swap
        s = list(str(num))
        s[max_digit_i], s[target_i] = s[target_i], s[max_digit_i]

        return int(''.join(s))

