'''
2023/07/18 daily challenge

doubly linked list approach
'''

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        self.key2node = dict()
        '''
        initialize a dummy head & tail.
        
        the node next to the head is the least recently used node.
        the node prior to the tail is the most recently used node.
        '''
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __delete(self, node):
        '''
        link the previous and next node directly.
        '''
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def __insert(self, node):
        '''
        attach the node to the last node prior from the tail.
        '''
        last_node = self.tail.prev
        
        node.prev = last_node
        node.next = self.tail
        
        last_node.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        node = self.key2node.get(key)
        if node is None:
            return -1
        
        '''
        move the node to the end of doubly linked list
        '''
        self.__delete(node)
        self.__insert(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.key2node.get(key)
        if node:
            self.__delete(node)
            node.value = value
        else:
            node = Node(key, value)
            self.key2node[key] = node
        
        self.__insert(node)
        
        # time to evict the least recently used node
        if len(self.key2node) > self.capacity:
            lru_node = self.head.next
            self.__delete(lru_node)
            del self.key2node[lru_node.key]

