'''
2022/09/03 daily challenge
learnt from official solutions

DFS ver
'''

class Solution1:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = list()
        
        # as 2 <= n <= 9 constraint applied by the judge,
        # no need to deal with n=1 special case here.
        # inner dfs() function cannot generate '0' answer.
        #
        # if n == 1: return [i for i in range(0,10)]
        
        # fast returns for special case: k=0
        if k == 0:
            return [int(''.join(str(i)*n)) for i in range(1,10)]
        
        def dfs(rem: int, snum: str):
            '''
            :param rem: remaining digits to be generated
            :type rem: int
            :param snum: string of generated digits
            :type snum: str
            
            special case not handled: n=1 or k=0
            '''
            if not rem:
                return ans.append(int(snum))
            
            tail_digit = int(snum[-1])
            next_digits = [tail_digit + k, tail_digit - k]
            
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    dfs(rem-1, snum + str(next_digit))
        
        for num in range(1, 10):
            # leftmost digit of number generated here.
            dfs(n-1, str(num))
        
        return ans

'''
BFS ver
'''

class Solution2:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # fast returns for special case: k=0
        if k == 0:
            return [int(''.join(str(i)*n)) for i in range(1,10)]

        # treat each digit as a level of tree
        # and generate every level of digit in once. (== breadth first)
        # generate initial level of digit.
        ans = [digit for digit in range(1,10)]
        
        for _ in range(n-1):
            new_ans = []  # ans with appended right digit
            
            for num in ans:
                tail_digit = num % 10
                next_digits = [tail_digit + k, tail_digit - k]
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_ans.append(num * 10 + next_digit)

            # certain level of digit generated, time to next level.
            ans = new_ans

        return ans
