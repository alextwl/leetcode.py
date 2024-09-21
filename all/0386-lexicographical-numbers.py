'''
2024/09/21 daily challenge

depth first search approach
'''


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(curr_val):
            if curr_val > n:
                return

            ans.append(curr_val)

            for child in range(10):
                next_val = curr_val * 10 + child
                if next_val <= n:
                    dfs(next_val)
                else:
                    break

        for i in range(1, 10):
            dfs(i)

        return ans

