'''
2024/09/21 daily challenge
2025/06/08 daily challenge

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


'''
backtracking without recursive function
'''


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        v = 1
        # flatten the sequence of DFS calls
        # since there're n numbers, we'll visit & append the ans n times exactly
        for _ in range(n):
            ret.append(v)
            if (next_num := v * 10) <= n:
                v = next_num
            else:
                if v >= n:
                    v //= 10
                v += 1
                while v % 10 == 0:
                    v //= 10
        return ret

