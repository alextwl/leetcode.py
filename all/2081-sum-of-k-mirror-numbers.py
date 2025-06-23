'''
2025/06/23 daily challenge

generate palindromes in binary search style

learnt from official editorial 1:
https://leetcode.com/problems/sum-of-k-mirror-numbers/editorial/#approach-1-binary-search
'''


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_k_mirror(v):
            dig = []
            while v:
                v, rem = divmod(v, k)
                dig.append(rem)
            return dig == dig[::-1]
        
        left = 1  # left bound of first half of 10-base palindrome
        cnt = 0  # number of increasing order
        ans = 0  # the sum
        while cnt < n:
            # construct 10-base palindromes
            right = left * 10
            # op=0: odd-length, op=1: even-length palindromes
            for op in [0, 1]:
                for i in range(left, right):
                    if cnt == n:
                        break
                    combined = i
                    # generate the last half of palindrome (without the center digit if existed)
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    # verify if it's also a k-base palindrome
                    if is_k_mirror(combined):
                        cnt += 1
                        ans += combined
            left = right
        return ans

