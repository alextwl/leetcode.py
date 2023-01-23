'''
2023/01/23 daily challenge

Set + counter approach
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = {person for person in range(1,n+1)}  # initially all people are candidates of town judge
        toBeTrusted = [0] * (n+1)

        for a, b in trust:
            candidates.discard(a)
            toBeTrusted[b] += 1
        
        max_trust = n-1
        for person in candidates:
            if toBeTrusted[person] == max_trust:
                # n-1 people trusts this person
                # town judge found
                return person

        # town judge not found
        return -1

