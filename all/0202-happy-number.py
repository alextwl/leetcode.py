'''
Cycle finding (two pointer) approach

learnt from official solution.

note the official solution provides advanced math approach
which observed a cycle which is always the same for all cases without ending in 1.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(num: int) -> int:
            '''
            sum the squares of each digit.
            
            39 -> 9**2 + 3**2
            '''
            ret = 0
            while(num > 0):
                num, digit = divmod(num, 10)
                ret += digit**2
            return ret
        
        slow, fast = n, square_sum(n)

        while(fast != 1 and slow != fast):
            '''
            let the slow and the fast go forward by different steps (1 and 2)
            and the fast will eventually catch up with the slow on the same number
            if a cycle exists. (Floyd's algorithm)
            '''
            slow = square_sum(slow)
            fast = square_sum(square_sum(fast))

        return fast == 1

