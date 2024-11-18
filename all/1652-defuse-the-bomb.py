'''
2024/11/18 daily challenge

sliding window approach
'''


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0] * n

        code = code * 2

        if k > 0:
            window_sum = 0
            for j in range(1, k + 1):
                window_sum += code[j]
            ans = [window_sum]
            right = k + 1
            for left in range(1, n):
                window_sum += code[right] - code[left]
                right += 1
                ans.append(window_sum)
        else:
            window_sum = 0
            k = -k
            for j in range(n - 1, n - k - 1, -1):
                window_sum += code[j]
            ans = [window_sum]
            left = n - k
            for right in range(n, n * 2 - 1):
                window_sum += code[right] - code[left]
                left += 1
                ans.append(window_sum)

        return ans

