'''
2023/09/01 daily challenge

math approach
'''


class Solution:
    def countBits(self, n: int) -> List[int]:
        # base case
        if n == 0:
            return [0]

        '''
        start from n < 2**1, iterate every power of 2 until n.
        '''
        ans = [0, 1]
        while(len(ans) <= n):
            '''
            reuse the previous results and generate next batch of power.
            
            e.g.
            0 --> 0b0  -> 0
            1 --> 0b1  -> 1
            2 --> 0b10 -> 1
            3 --> 0b11 -> 2
            
            so the ans of 4 ~ 7 are:
            4 --> 0b100 -> 1 == f(0)+1
            5 --> 0b101 -> 2 == f(1)+1
            6 --> 0b110 -> 2 == f(2)+1
            7 --> 0b111 -> 3 == f(3)+1
            '''
            ans.extend([i+1 for i in ans])

        return ans[:n+1]

