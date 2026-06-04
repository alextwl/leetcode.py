'''
2026/06/04 daily challenge

linear enumeration (brute force) approach (non-casting ver)
'''


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        num1 = max(num1, 100)  # any number < 100 has a waviness of 0

        # build an array of reversed digits couting from num1
        # (prevent the later brute force block from casting between int and str)
        ctr_list = []
        i, v = 0, num1
        while v:
            v, rem = divmod(v, 10)
            ctr_list.append(rem)
            i += 1

        wave = 0
        # brute force all numbers in the range
        for ctr_int in range(num1, num2 + 1):
            it = iter(ctr_list)
            v0 = next(it)
            v1 = next(it)
            for v2 in it:
                if (v0 < v1 and v1 > v2) or (v0 > v1 and v1 < v2):
                    wave += 1
                v0, v1 = v1, v2
            
            # increment array counter
            i = 0
            carry = 1
            while carry:
                if i == len(ctr_list):
                    ctr_list.append(1)
                else:
                    ctr_list[i] += 1
                if ctr_list[i] == 10:
                    ctr_list[i] = 0
                    i += 1
                else:
                    carry = 0

        return wave

