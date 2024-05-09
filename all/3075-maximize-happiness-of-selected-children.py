'''
2024/05/09 daily challenge

sort + greedy method approach
'''


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        happiness = happiness[:k]
        
        ans = 0
        for i, v in enumerate(happiness):
            v -= i
            if v < 0:
                break
            else:
                ans += v

        return ans

