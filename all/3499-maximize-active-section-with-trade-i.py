'''
2026/07/21 daily challenge

greedy method approach
'''


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # convert to segments
        # for an active segment, length of segment == segs[i]
        # for an inactive segment, length of segment == -segs[i]
        segs = []
        val = 0  # length of current continguous segment
        actives = 0   # original total active sections
        for c in s:
            if c == '1':
                if val < 0:
                    segs.append(val)
                    val = 1
                else:
                    val += 1
            else:
                if val > 0:
                    segs.append(val)
                    actives += val
                    val = -1
                else:
                    val -= 1
        segs.append(val)
        if val > 0:
            actives += val

        # determine whether to add augments or not.
        if segs[0] < 0:
            segs.insert(0, 0)
        if segs[-1] < 0:
            segs.append(0)

        if len(segs) < 5:
            # no valid trade is possible
            return actives

        max_gain = 0
        # scan segments in [active, inactive, active, inactive, active] group
        # and maximize the sum of these two inactive segments.
        for i in range(1, len(segs) - 2, 2):
            max_gain = max(max_gain, -segs[i] - segs[i + 2])
        return actives + max_gain

