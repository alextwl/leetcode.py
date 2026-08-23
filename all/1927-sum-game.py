'''
2926/08/23 daily challenge

mathematical induction approach

learnt from official editorial:
https://leetcode.com/problems/sum-game/editorial/#approach-guess--mathematical-induction-verification
'''


class Solution:
    def sumGame(self, num: str) -> bool:
        def get(s):
            dig_sum = 0
            q_mark = 0
            for c in s:
                if c == '?':
                    q_mark += 1
                else:
                    dig_sum += int(c)
            return dig_sum, q_mark

        n = len(num)
        n0, q0 = get(num[:n // 2])
        n1, q1 = get(num[n // 2:])

        return (q0 + q1) % 2 == 1 or n0 - n1 != (q1 - q0) * 9 // 2

