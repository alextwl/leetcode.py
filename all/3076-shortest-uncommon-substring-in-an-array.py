'''
brute force all substrings.
'''


import collections


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        # subs[sub_string] = {indices of arr}
        subs = collections.defaultdict(set)

        for i, s in enumerate(arr):
            for j in range(len(s)):
                for k in range(j + 1, len(s) + 1):
                    subs[s[j:k]].add(i)

        ans = []
        for i, s in enumerate(arr):
            # valid substring that haven't seen in other strings in arr.
            valids = []
            for j in range(len(s)):
                for k in range(j + 1, len(s) + 1):
                    curr_sub = s[j:k]
                    if len(subs[curr_sub]) == 1:
                        valids.append(curr_sub)
            # do lexicographically sorting
            valids.sort(key=lambda x: (len(x), x))
            ans.append(valids[0] if valids else "")

        return ans

