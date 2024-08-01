'''
2024/07/29 daily challenge

dynamic programming approach (tabulation)
'''


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0
        
        inc_teams = [{i: 0 for i in range(1,4)} for _ in range(n)]
        dec_teams = [{i: 0 for i in range(1,4)} for _ in range(n)]
        
        # base case: each soldier forms a team of single member
        for i in range(n):
            inc_teams[i][1] = 1
            dec_teams[i][1] = 1
        
        for cnt in [2, 3]:
            # count all increasing/decreasing teams of 2 & 3 members
            for i in range(n):
                for j in range(i + 1, n):
                    if rating[j] > rating[i]:
                        inc_teams[j][cnt] += inc_teams[i][cnt-1]
                    if rating[j] < rating[i]:
                        dec_teams[j][cnt] += dec_teams[i][cnt-1]
        
        for a, b in zip(inc_teams, dec_teams):
            ans += a[3] + b[3]

        return ans


'''
binary indexed tree (Fenwick tree) approach
'''


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def update_bit(tree, i, cnt):
            while i < len(tree):
                tree[i] += cnt
                i += i & (-i)  # move to the next node of binary indexed tree
        
        def get_prefix_sum(tree, i):
            prefix = 0
            while i > 0:
                prefix += tree[i]
                i -= i & (-i)  # move to the parent node
            return prefix
        
        max_val = max(rating)
        left_tree = [0] * (max_val + 1)
        right_tree = [0] * (max_val + 1)
        
        # build right side tree
        for v in rating:
            update_bit(right_tree, v, 1)
        
        ans = 0
        # build left side tree
        for v in rating:
            update_bit(right_tree, v, -1)  # remove from right tree
            
            smaller_left_sum = get_prefix_sum(left_tree, v - 1)
            smaller_right_sum = get_prefix_sum(right_tree, v - 1)
            larger_left_sum = get_prefix_sum(left_tree, max_val) - get_prefix_sum(left_tree, v)
            larger_right_sum = get_prefix_sum(right_tree, max_val) - get_prefix_sum(right_tree, v)
            
            # accumulate increasing/decreasing pairs
            ans += smaller_left_sum * larger_right_sum + larger_left_sum * smaller_right_sum
            
            update_bit(left_tree, v, 1)  # add to left tree
        
        return ans

