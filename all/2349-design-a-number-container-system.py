'''
2025/02/08 daily challenge

hashmap + min heap approach
'''


import heapq


class NumberContainers:
    def __init__(self):
        self.slots = dict()
        self.num_heaps = dict()  # num to index min-heap

    def change(self, index: int, number: int) -> None:
        self.slots[index] = number
        if number not in self.num_heaps:
            self.num_heaps[number] = list()
        heapq.heappush(self.num_heaps[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_heaps:
            return -1
        h = self.num_heaps[number]
        while h:
            if self.slots[h[0]] == number:
                # hit
                return h[0]
            # miss
            heapq.heappop(h)
        return -1

