'''
2025/04/10 daily challenge

combinatorial approach

learnt from official editorial 2:
https://leetcode.com/problems/count-the-number-of-powerful-integers/editorial/#approach-2-combinatorial-mathematics
'''


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def comb(a):
            # count all possibilities <= a
            la, ls = len(a), len(s)
            if la < ls:
                # when the length of a is shorter than s,
                # no value ends with s.
                return 0
            if la == ls:
                # the only valid value is s itself if it's <= a.
                return int(a >= s)

            count = 0
            suffix = a[la-ls:]
            prefix_len = la - ls

            # count combinations of prefix part
            for i in range(prefix_len):
                v = int(a[i])
                if limit < v:
                    # all digits: [0, limit]
                    count += (limit + 1) ** (prefix_len - i)
                    return count
                # 1st digit: [0, v], remainings: [0, limit]
                count += v * (limit + 1) ** (prefix_len - i - 1)

            if suffix >= s:
                # count the only case with max prefix.
                count += 1
            return count

        top = str(finish)
        ground = str(start - 1)  # the last number smaller than start

        return comb(top) - comb(ground)

