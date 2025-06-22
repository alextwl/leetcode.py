'''
2025/06/22 daily challenge
'''


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = [s[i*k:(i+1)*k] for i in range((len(s) + k - 1) // k)]
        if len(ans[-1]) < k:
            ans[-1] = ans[-1] + (k - len(ans[-1])) * fill
        return ans

