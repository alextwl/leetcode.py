'''
greedy method approach

select smallest for 'I' and largest for 'D' greedily.

(the editorial named it 'Ad-Hoc')
'''


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)
        arr = []
        for c in s:
            if c == 'I':
                arr.append(left)
                left += 1
            else:
                arr.append(right)
                right -= 1
        # append the last number
        # assert(left == right)
        arr.append(left)
        return arr

