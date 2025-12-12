'''
2025/12/12 daily challenge

sorting + simulation approach
'''


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        evts = [(ev[0] == "M", int(ts), s) for ev, ts, s in events]
        # sorted by:
        # (1) timestamp
        # (2) OFFLINE, MESSAGE
        evts.sort(key=lambda x: (x[1], x[0]))

        all_count = 0
        ans = [0] * numberOfUsers
        offlined = dict()
        for ev, ts, s in evts:
            if ev:
                # MESSAGE
                if s[0] == 'A':
                    # ALL
                    all_count += 1
                elif s[0] == 'H':
                    # HERE
                    for i in range(numberOfUsers):
                        if i in offlined:
                            if offlined[i] <= ts:
                                ans[i] += 1
                                del offlined[i]
                        else:
                            ans[i] += 1
                else:
                    # specific user list
                    # note this can mention even the offline users.
                    for i in map(int, s[2:].split(' id')):
                        ans[i] += 1
            else:
                # OFFLINE
                offlined[int(s)] = ts + 60
        return [cnt + all_count for cnt in ans]

