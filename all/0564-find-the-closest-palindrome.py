'''
2024/08/24 daily challenge

exhaustive method approach
'''


class Solution:
    def nearestPalindromic(self, num_str: str) -> str:
        n = len(num_str)

        if n == 1:
            return str(int(num_str) - 1)

        candidates = []

        # populate the substring of the first half digits **including center if the length is odd.**
        first_half_str = num_str[:(n>>1) + (n & 1)]

        # case 1: form a palindrome based on first half of input digits.
        # note not including itself.
        s = first_half_str + first_half_str[(n>>1) -1::-1]
        if s != num_str:
            candidates.append(int(s))
        # case 2: form a palindrome based on first half - 1
        new_half_str = str(int(first_half_str) - 1)
        s = new_half_str + new_half_str[(n>>1)-1::-1]
        candidates.append(int(s))
        # case 3: form a palindrome based on first half + 1
        new_half_str = str(int(first_half_str) + 1)
        s = new_half_str + new_half_str[(n>>1)-1::-1]
        candidates.append(int(s))
        # case 4: nearest smaller all nine's
        candidates.append(10 ** (n-1) - 1)
        # case 5: nearest larger 1_000...000_1 form of number
        candidates.append(10 ** n + 1)
        
        num_int = int(num_str)
        min_diff = float('inf')
        ans = 0
        for v in candidates:
            diff = abs(v - num_int)
            if diff == 0:
                # note not including itself.
                continue
            if diff < min_diff:
                min_diff = diff
                ans = v
            elif diff == min_diff and v < ans:
                ans = v

        return str(ans)

