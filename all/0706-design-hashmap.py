'''
2023/10/04 daily challenge

Knuth's multiplicative hash approach

similar to problem 705
'''

P = 2097593
W = 20
M = 14  # math.ceil(log(at most 10**4 calls, 2)) == 14


class MyHashMap:
    def __init__(self):
        self.shifts = W - M
        self.buckets = [[] for _ in range(1<<M)]

    def _h(self, key:int) -> int:
        return ((P * key) & (1 << W) - 1) >> self.shifts

    def put(self, key: int, value: int) -> None:
        hash_key = self._h(key)
        bucket = self.buckets[self._h(key)]
        for pair in bucket:
            if pair[0] == key:
                # update existed key
                pair[1] = value
                break
        else:
            # insert a new key
            bucket.append([key, value])
    
    def get(self, key: int) -> int:
        hash_key = self._h(key)
        for k, v in self.buckets[hash_key]:
            if k == key:
                # key found
                return v
        
        return -1

    def remove(self, key: int) -> None:
        hash_key = self._h(key)
        bucket = self.buckets[self._h(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                self.buckets[self._h(key)] = bucket[:i] + bucket[i+1:]
                break

