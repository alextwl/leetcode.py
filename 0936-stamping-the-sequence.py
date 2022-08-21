'''
2022/08/21 daily challenge
reverse approach, learnt from
https://leetcode.com/problems/stamping-the-sequence/solution/893736
time=O(n**3) but I can understand more easily than official solution

answer is not guaranteed to have minimal stamps
as some initial stamps may be overrided completely by latter ones.
'''
class Solution:
    def equals(self, target, stamp, i):
        '''
        determine i-th window of target was stamped or not
        '''
        for j, c in enumerate(stamp):
            if not(target[i+j] == c or target[i+j] == '?'):
                return False
        return True

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # make a copy of target
        tcopy = [c for c in target]
        
        N, M = len(tcopy), len(stamp)
        
        ans = []
        checked = set()
        
        # examine i-th window of target
        for i in range(N-M+1):
            # first match is always the last stamp
            # in the range of [0, i]
            if self.equals(tcopy, stamp, i):
                # Do reverse comparsion from i-th window to 0-th window.
                for x in range(i, -1, -1):
                    if x in checked:
                        # x-th window was already checked.
                        # no need to proceed remaining windows
                        # because they were also checked previously.
                        break
                    checked.add(x)
                    # may skip optional stamp here
                    # if all chars in current window were already reset to '?'.
                    #
                    #     if all([c == '?' for c in tcopy[x:x+M]]):
                    #         continue
                    if self.equals(tcopy, stamp, x):
                        # x-th window was stamped.
                        # reset the window to unstamped status.
                        ans.append(x)
                        tcopy[x:x+M] = ['?'] * M

        if all([c == '?' for c in tcopy]):
            # all chars in target can be unstamped, answer exists.
            # because we check stamps in target reversely,
            # the sequence of ans should be reversed too.
            return ans[::-1]
        
        # ans not found
        return []
