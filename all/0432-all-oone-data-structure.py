'''
2024/09/29 daily challenge

hash + doubly linked list approach

store frequencies by linked list, and map strings to linked list nodes.

learnt from official solution:
https://leetcode.com/problems/all-oone-data-structure/solution/
'''


class Node:
    def __init__(self, freq=0, prev=None, next=None):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        
        self.key2node = dict()

    def inc(self, key: str) -> None:
        if key in self.key2node:
            node = self.key2node[key]
            
            freq = node.freq
            newfreq = freq + 1
            node.keys.remove(key)
            print(key)
            child = node.next
            if child == self.tail or child.freq != newfreq:
                # add a new node for newfreq
                newnode = Node(freq=newfreq, prev=node, next=child)
                newnode.keys.add(key)
                self.key2node[key] = newnode
                node.next = newnode
                child.prev = newnode
            else:
                child.keys.add(key)
                self.key2node[key] = child
            
            # remove empty node
            if not node.keys:
                parent = node.prev
                child = node.next
                parent.next = child
                child.prev = parent
        else:
            # key not found
            if self.head.next == self.tail or self.head.next.freq > 1:
                newnode = Node(freq=1, prev=self.head, next=self.head.next)
                newnode.keys.add(key)
                self.key2node[key] = newnode
                self.head.next.prev = newnode
                self.head.next = newnode
            else:
                self.head.next.keys.add(key)
                self.key2node[key] = self.head.next

    def dec(self, key: str) -> None:
        if key not in self.key2node:
            return
        
        node = self.key2node[key]
        freq = node.freq
        newfreq = freq - 1
        node.keys.remove(key)
        
        if freq == 1:
            del self.key2node[key]
        else:
            parent = node.prev
            if parent == self.head or parent.freq != newfreq:
                newnode = Node(freq=newfreq, prev=parent, next=node)
                newnode.keys.add(key)
                self.key2node[key] = newnode
                parent.next = newnode
                node.prev = newnode
            else:
                parent.keys.add(key)
                self.key2node[key] = parent
        
        # remove empty node
        if not node.keys:
            parent = node.prev
            child = node.next
            parent.next = child
            child.prev = parent

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

