'''
2022/10/29 daily challenge

greddy approach, learnt from official solution (see the inequality proofs)

the bloom line = sum(day of plants) + days of last bloom

planting the seeds by descending growth time is optimal.
'''

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # sort the seed index by descending growth time
        seed_seq = sorted(range(len(growTime)), key=lambda x: -growTime[x])
        
        t = 0  # the minimum days of bloom line
        s = 0  # the plant time elapsed
        
        for seed in seed_seq:
            s += plantTime[seed]
            '''
            the bloom line is the day of the last bloom, not necessary the last seed planted,
            some seeds may bloom earlier before previous seeds,
            so use max() here to evaluate the bloom line.
            '''
            t = max(t, s + growTime[seed])
        
        return t
