'''
2022/10/18 daily challenge
2025/04/18 daily challenge

intuitive approach.

the description of the problem is quite confusing,
write some examples before coding.

n=5 == say "1211" == one 1 + one 2 + two 1's == "111221"
n=6 == say "111221" == three 1's + two 2's + one 1 == "312211"
n=7 == say "312211" == one 3 + one 1 + two 2's + two 1's == "13112221"
... and so on.
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        def c2s(nlist: list[int]) -> list:
            '''
            :param nlist: a list consisting of numbers splited from main arg `n`.
            :type nlist: list
            :return: a list of numbers of countAndSay result.
            '''
            current = None
            count = 0
            ret = []
            
            for num in nlist:
                if num != current:
                    # say last number's count
                    if current != None:
                        # "<count> <number>['s]", e.g. say "2" == one 2, say "33" == two 3's.
                        ret.extend([count, current])
                    # and reset to new number
                    current = num
                    count = 0
                # add count for current number.
                count += 1
            
            # say the latest number's count
            ret.extend([count, current])
            
            return ret
        
        last_c2s = [1]  # base case
        
        for _ in range(2, n+1):
            '''
            convert the sequence which is the return value from last c2s() call.
            '''
            last_c2s = c2s(last_c2s)
        
        return ''.join(map(str, last_c2s))  # say the digit string.


'''
recursion approach
'''


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        s = self.countAndSay(n - 1)
        prev = s[0]
        cnt = 0
        t = []
        for c in s:
            if c != prev:
                t.append(str(cnt))
                t.append(prev)
                prev = c
                cnt = 1
            else:
                cnt += 1
        t.append(str(cnt))
        t.append(prev)
        return ''.join(t)

