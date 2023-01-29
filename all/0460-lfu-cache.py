'''
2023/01/29 daily challenge

OrderedDict approach
'''

import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.freq = 0


class LFUCache:

    def __init__(self, capacity: int):
        # freq -> OrderedDict of keys -> node
        self._freq = collections.defaultdict(lambda: collections.OrderedDict())
        # keys -> node
        self._cache = dict()
        self.capacity = capacity
        self.minFreq = 0

    def _get(self, key: int) -> Node:
        '''
        Get the node instance by key.

        it increments the frequency of the key if available.
        '''
        node = self._cache.get(key, None)
        if node is None:
            return None
        
        # retrieve current (old) frequency of key
        oldFreq = node.freq
        # increment the frequency
        node.freq += 1
        # remove the key from the old frequency's list
        del self._freq[oldFreq][key]
        # push to the new frequency's list
        self._freq[node.freq][key] = node
        # update the minimum frequency
        if self.minFreq == oldFreq and not self._freq[oldFreq]:
            self.minFreq += 1

        return node

    def get(self, key: int) -> int:
        '''
        Wrapper of self._get(), it returns the value instead of node.
        '''
        if (node := self._get(key)) is None:
            return -1

        return node.value

    def put(self, key: int, value: int) -> None:
        '''
        Insert or update the key with the value.
        '''
        if self.capacity == 0:
            # corner case for testcase 4: zero capacity of a cache
            return
        if key in self._cache:
            '''
            if the key is already present, updating it is also incrementing its frequency.
            '''
            node = self._get(key)
            node.value = value
        else:
            if len(self._cache) == self.capacity:
                # the cache is full, pop LFU first
                lfu_key, lfu_node = self._freq[self.minFreq].popitem(last=False)
                del self._cache[lfu_key]
            # add new key with zero frequency
            node = Node(value)
            self._cache[key] = node
            self._freq[0][key] = node
            self.minFreq = 0

