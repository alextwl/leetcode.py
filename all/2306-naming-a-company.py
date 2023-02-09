'''
2023/02/09 daily challenge

suffix group approach
learnt from official solution

valid case:
for ("coffee", "donuts"),
"offee" in 'c' group + "onuts" in 'd' group -> "doffee conuts" & "conuts doffee",
two new ideas create **double** new names.

invalid cases:
(1) for ("coffee", "caffeine"),
"offee" + "affeine" in the same 'c' group -> "caffeine" + "coffee" are invalid because both are already in the ideas.
(2) for ("coffee", "toffee"),
the same "offee" suffix in 'c' group & 't' group -> "toffee" + "coffee" are invalid because both are already in the ideas.
(3) for ("coffee", "time", "toffee"),
"offee" in 'c' group + "ime" in 't' group -> "toffee" + "cime" are invalid because one of the new name ("toffee") is already in the ideas.

so the invalid cases (suffixes in the same group & same suffixes in different groups) cannot be counted.
'''

import string


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        p2suffixes = {c: set() for c in string.ascii_lowercase}
        for s in ideas:
            p2suffixes[s[0]].add(s[1:])
        
        ans = 0
        for i in range(25):  # [a-y] excluding z
            c1 = string.ascii_lowercase[i]
            for c2 in string.ascii_lowercase[i+1:]:
                invalid_group_len = len(p2suffixes[c1] & p2suffixes[c2])
                ans += (len(p2suffixes[c1]) - invalid_group_len) * (len(p2suffixes[c2]) - invalid_group_len) * 2
        
        return ans

