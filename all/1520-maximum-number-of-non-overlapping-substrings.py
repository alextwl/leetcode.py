'''
2026/09/18 daily challenge

interval merger + greedy method approach
'''


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        left = dict()
        right = dict()

        for i, c in enumerate(s):
            if c not in left:
                left[c] = i
            right[c] = i

        # intvals: [left pos in s, right pos in s]
        # c2i[c] = index of char in intvals
        intvals = []
        c2i = dict()
        for i, c in enumerate(left.keys()):
            intvals.append([left[c], right[c]])
            c2i[c] = i

        for i in range(len(intvals)):
            si = intvals[i][0]  # leftmost index in s for current char
            while si <= intvals[i][1]:
                j = c2i[s[si]]
                # check if not(intvals[i] contains intvals[j])
                if not (intvals[i][0] <= intvals[j][0] and intvals[j][1] <= intvals[i][1]):
                    # merge all intervals **where chars seen before intvals[i][1] in s**
                    intvals[i][0] = min(intvals[i][0], intvals[j][0])
                    intvals[i][1] = max(intvals[i][1], intvals[j][1])
                si += 1

        # order by rightbound asc, and then leftbound desc
        # we'd like to select shorter intervals greedily
        intvals.sort(key=lambda x: (x[1], -x[0]))

        ans = []
        rightmost = -1  # rightbound of the last interval picked up
        for l, r in intvals:
            if l > rightmost:
                rightmost = r
                ans.append(s[l:r+1])
        return ans

