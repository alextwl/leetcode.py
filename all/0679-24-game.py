'''
2025/08/18 daily challenge

brute force backtracking approach

since we were brute-forcing all possible combinations of evaluation with
2 values until the stack remains only one value, the actual positions of
parentheses are irrelevant.
'''


EPSILON = 1e-6  # 10**(-6), close-enough factor


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        nums = list(map(float, cards))

        def bt(arr):
            if len(arr) == 1:
                return abs(arr[0] - 24.0) < EPSILON
            
            # pick two cards a & b
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if i == j: continue

                    a, b = arr[i], arr[j]
                    remains = [v for k, v in enumerate(arr) if k not in [i, j]]

                    all_evals = [a + b, a - b, b - a, a * b]
                    # prevent zero division and invalid gradients
                    if abs(b) > EPSILON:
                        all_evals.append(a / b)
                    if abs(a) > EPSILON:
                        all_evals.append(b / a)
                    
                    # brute force all combinations
                    for v in all_evals:
                        remains.append(v)
                        if bt(remains):
                            return True
                        remains.pop()
            return False
        return bt(nums)

