'''
2024/05/26 daily challenge

state machine + bottom-up dynamic programming approach

learnt from official solution 3:
https://leetcode.com/problems/student-attendance-record-ii/solution/
'''

MOD = 1_000_000_007


class Solution:
    def checkRecord(self, n: int) -> int:
        curr_states = [[0] * 3 for _ in range(2)]
        next_states = [[0] * 3 for _ in range(2)]
        
        curr_states[0][0] = 1
        
        for _ in range(n):
            for absent_count in range(2):
                for late_count in range(3):
                    # P
                    next_states[absent_count][0] = \
                        (next_states[absent_count][0] + curr_states[absent_count][late_count]) % MOD
                    # A
                    if not absent_count:
                        next_states[absent_count + 1][0] = \
                            (next_states[absent_count + 1][0] + curr_states[absent_count][late_count]) % MOD
                    # L
                    if late_count < 2:
                        next_states[absent_count][late_count + 1] = \
                            (next_states[absent_count][late_count + 1] + curr_states[absent_count][late_count]) % MOD
            # prev, curr = curr, new
            curr_states = next_states
            next_states = [[0] * 3 for _ in range(2)]
        
        return sum(sum(row) for row in curr_states) % MOD

